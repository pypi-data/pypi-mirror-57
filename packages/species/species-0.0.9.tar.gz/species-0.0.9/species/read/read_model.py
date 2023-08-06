"""
Module for reading atmospheric models.
"""

import os
import math
import configparser

import h5py
import spectres
import numpy as np

from scipy.interpolate import RegularGridInterpolator

from species.analysis import photometry
from species.core import box, constants
from species.data import database
from species.read import read_filter, read_calibration
from species.util import read_util


class ReadModel:
    """
    Read atmospheric model spectra.
    """

    def __init__(self,
                 model,
                 wavelength,
                 teff=None):
        """
        Parameters
        ----------
        model : str
            Model name.
        wavelength : tuple(float, float) or str
            Wavelength range (micron) or filter name. Full spectrum is used if set to None.
        teff : tuple(float, float)
            Effective temperature (K) range. Restricting the temperature range will speed up the
            computation.

        Returns
        -------
        NoneType
            None
        """

        self.model = model
        self.teff = teff

        self.spectrum_interp = None
        self.wl_points = None
        self.wl_index = None

        if isinstance(wavelength, str):
            self.filter_name = wavelength
            transmission = read_filter.ReadFilter(wavelength)
            self.wavelength = transmission.wavelength_range()

        else:
            self.filter_name = None
            self.wavelength = wavelength

        config_file = os.path.join(os.getcwd(), 'species_config.ini')

        config = configparser.ConfigParser()
        config.read_file(open(config_file))

        self.database = config['species']['database']

    def open_database(self):
        """
        Returns
        -------
        h5py._hl.files.File
            Database.
        """

        config_file = os.path.join(os.getcwd(), 'species_config.ini')

        config = configparser.ConfigParser()
        config.read_file(open(config_file))

        database_path = config['species']['database']

        h5_file = h5py.File(database_path, 'r')

        try:
            h5_file['models/'+self.model]

        except KeyError:
            h5_file.close()
            species_db = database.Database()
            species_db.add_model(self.model, self.wavelength, self.teff)
            h5_file = h5py.File(database_path, 'r')

        return h5_file

    def wavelength_points(self,
                          hdf5_file):
        """
        Parameters
        ----------
        hdf5_file : h5py._hl.files.File
            hdf5_file.

        Returns
        -------
        numpy.ndarray
            Wavelength points (micron).
        numpy.ndarray
            Array with the size of the original wavelength grid. The booleans indicate if a
            wavelength point was used.
        """

        wl_points = np.asarray(hdf5_file['models/'+self.model+'/wavelength'])

        if self.wavelength is None:
            wl_index = np.ones(wl_points.shape[0], dtype=bool)

        else:
            wl_index = (wl_points > self.wavelength[0]) & (wl_points < self.wavelength[1])
            index = np.where(wl_index)[0]

            if index[0]-1 >= 0:
                wl_index[index[0] - 1] = True

            if index[-1]+1 < wl_index.size:
                wl_index[index[-1] + 1] = True

        return wl_points[wl_index], wl_index

    def interpolate(self):
        """
        Returns
        -------
        NoneType
            None
        """

        h5_file = self.open_database()

        flux = np.asarray(h5_file['models/'+self.model+'/flux'])
        teff = np.asarray(h5_file['models/'+self.model+'/teff'])
        logg = np.asarray(h5_file['models/'+self.model+'/logg'])

        if self.wl_points is None:
            self.wl_points, self.wl_index = self.wavelength_points(h5_file)

        if self.model in ('drift-phoenix', 'bt-nextgen', 'petitcode-cool-clear'):
            feh = np.asarray(h5_file['models/'+self.model+'/feh'])

            points = (teff, logg, feh)
            flux = flux[:, :, :, self.wl_index]

        elif self.model in ('bt-settl', 'ames-dusty', 'ames-cond'):
            points = (teff, logg)
            flux = flux[:, :, self.wl_index]

        elif self.model == 'petitcode-cool-cloudy':
            feh = np.asarray(h5_file['models/petitcode-cool-cloudy/feh'])
            fsed = np.asarray(h5_file['models/petitcode-cool-cloudy/fsed'])

            points = (teff, logg, feh, fsed)
            flux = flux[:, :, :, :, self.wl_index]

        elif self.model == 'petitcode-hot-clear':
            feh = np.asarray(h5_file['models/petitcode-hot-clear/feh'])
            co_ratio = np.asarray(h5_file['models/petitcode-hot-clear/co'])

            points = (teff, logg, feh, co_ratio)
            flux = flux[:, :, :, :, self.wl_index]

        elif self.model == 'petitcode-hot-cloudy':
            feh = np.asarray(h5_file['models/petitcode-hot-cloudy/feh'])
            co_ratio = np.asarray(h5_file['models/petitcode-hot-cloudy/co'])
            fsed = np.asarray(h5_file['models/petitcode-hot-cloudy/fsed'])

            flux = flux[:, :, :, :, :, self.wl_index]
            points = (teff, logg, feh, co_ratio, fsed)

        h5_file.close()

        self.spectrum_interp = RegularGridInterpolator(points=points,
                                                       values=flux,
                                                       method='linear',
                                                       bounds_error=False,
                                                       fill_value=np.nan)

    def get_model(self,
                  model_par,
                  specres=None,
                  magnitude=False):
        """
        Function to extract a model spectrum with a multidimensional interpolation of the model
        grid. The parameters values should therefore lie within the boundaries of the grid points
        that are stored in the database. The stored grid points can be inspected with
        :func:`~species.read.read_model.ReadModel.get_points`.

        Parameters
        ----------
        model_par : dict
            Model parameter values.
        specres : float
            Spectral resolution, achieved by smoothing with a Gaussian kernel. The original
            wavelength points are used if set to None. Using a high spectral resolution is
            computationally faster if the original wavelength grid has a fine sampling.
        magnitude : bool
            Normalize the spectrum with a flux calibrated spectrum of Vega and return the magnitude
            instead of flux density.

        Returns
        -------
        species.core.box.ModelBox
            Box with the model spectrum.
        """

        if 'mass' in model_par:
            mass = 1e3 * model_par['mass'] * constants.M_JUP  # [g]
            radius = math.sqrt(1e3 * constants.GRAVITY * mass / (10.**model_par['logg']))  # [cm]
            model_par['radius'] = 1e-2 * radius / constants.R_JUP  # [Rjup]

        if self.spectrum_interp is None:
            self.interpolate()

        if self.wavelength is None:
            wl_points = self.get_wavelength()
            self.wavelength = (wl_points[0], wl_points[-1])

        if self.model in ('drift-phoenix', 'bt-nextgen', 'petitcode-cool-clear'):
            parameters = [model_par['teff'],
                          model_par['logg'],
                          model_par['feh']]

        elif self.model in ('bt-settl', 'ames-dusty', 'ames-cond'):
            parameters = [model_par['teff'],
                          model_par['logg']]

        elif self.model == 'petitcode-cool-cloudy':
            parameters = [model_par['teff'],
                          model_par['logg'],
                          model_par['feh'],
                          model_par['fsed']]

        elif self.model == 'petitcode-hot-clear':
            parameters = [model_par['teff'],
                          model_par['logg'],
                          model_par['feh'],
                          model_par['co']]

        elif self.model == 'petitcode-hot-cloudy':
            parameters = [model_par['teff'],
                          model_par['logg'],
                          model_par['feh'],
                          model_par['co'],
                          model_par['fsed']]

        flux = self.spectrum_interp(parameters)[0]

        if 'radius' in model_par:
            model_par['mass'] = read_util.get_mass(model_par)

            if 'distance' in model_par:
                scaling = (model_par['radius']*constants.R_JUP)**2 / \
                          (model_par['distance']*constants.PARSEC)**2

                flux *= scaling

        if specres is not None:
            index = np.where(np.isnan(flux))[0]

            if index.size > 0:
                raise ValueError('Flux values should not contains NaNs. Please make sure that '
                                 'the parameter values and the wavelength range are within '
                                 'the grid boundaries as stored in the database.')

            flux = read_util.smooth_spectrum(wavelength=self.wl_points,
                                             flux=flux,
                                             specres=specres,
                                             size=11)

        if magnitude:
            quantity = 'magnitude'

            with h5py.File(self.database, 'r') as h5_file:
                try:
                    h5_file['spectra/calibration/vega']

                except KeyError:
                    h5_file.close()
                    species_db = database.Database()
                    species_db.add_spectrum('vega')
                    h5_file = h5py.File(self.database, 'r')

            readcalib = read_calibration.ReadCalibration(spectrum='vega', filter_name=None)
            calibbox = readcalib.get_spectrum()

            flux_vega, _ = spectres.spectres(new_spec_wavs=self.wl_points,
                                             old_spec_wavs=calibbox.wavelength,
                                             spec_fluxes=calibbox.flux,
                                             spec_errs=calibbox.error)

            flux = -2.5*np.log10(flux/flux_vega)

        else:
            quantity = 'flux'

        is_finite = np.where(np.isfinite(flux))[0]

        return box.create_box(boxtype='model',
                              model=self.model,
                              wavelength=self.wl_points[is_finite],
                              flux=flux[is_finite],
                              parameters=model_par,
                              quantity=quantity)

    def get_data(self,
                 model_par):
        """
        Function to extract a model spectra without interpolation for parameter values that are
        stored within the database. The stored grid points can be inspected with
        :func:`~species.read.read_model.ReadModel.get_points`.

        Parameters
        ----------
        model_par : dict
            Model parameter values. Only discrete values from the original grid are possible. Else,
            the nearest grid values are selected.

        Returns
        -------
        species.core.box.ModelBox
            Box with the model spectrum.
        """

        h5_file = self.open_database()

        wl_points, wl_index = self.wavelength_points(h5_file)

        flux = np.asarray(h5_file['models/'+self.model+'/flux'])
        teff = np.asarray(h5_file['models/'+self.model+'/teff'])
        logg = np.asarray(h5_file['models/'+self.model+'/logg'])

        if self.model in ('bt-settl', 'ames-cond', 'ames-dusty'):
            teff_index = np.argwhere(teff == model_par['teff'])[0]

            if not teff_index:
                raise ValueError('Temperature value not found.')

            teff_index = teff_index[0]
            logg_index = np.argwhere(logg == model_par['logg'])[0]

            if not logg_index:
                raise ValueError('Surface gravity value not found.')

            logg_index = logg_index[0]

            flux = flux[teff_index, logg_index, wl_index]

        elif self.model in ('drift-phoenix', 'bt-nextgen'):
            feh = np.asarray(h5_file['models/'+self.model+'/feh'])

            teff_index = np.argwhere(teff == model_par['teff'])[0]

            if not teff_index:
                raise ValueError('Temperature value not found.')

            teff_index = teff_index[0]
            logg_index = np.argwhere(logg == model_par['logg'])[0]

            if not logg_index:
                raise ValueError('Surface gravity value not found.')

            logg_index = logg_index[0]
            feh_index = np.argwhere(feh == model_par['feh'])[0]

            if not feh_index:
                raise ValueError('Metallicity value not found.')

            feh_index = feh_index[0]

            flux = flux[teff_index, logg_index, feh_index, wl_index]

        elif self.model == 'petitcode-hot-clear':
            feh = np.asarray(h5_file['models/'+self.model+'/feh'])
            co_ratio = np.asarray(h5_file['models/'+self.model+'/co'])

            teff_index = np.argwhere(teff == model_par['teff'])[0]

            if not teff_index:
                raise ValueError('Temperature value not found.')

            teff_index = teff_index[0]
            logg_index = np.argwhere(logg == model_par['logg'])[0]

            if not logg_index:
                raise ValueError('Surface gravity value not found.')

            logg_index = logg_index[0]
            feh_index = np.argwhere(feh == model_par['feh'])[0]

            if not feh_index:
                raise ValueError('Metallicity value not found.')

            feh_index = feh_index[0]
            co_index = np.argwhere(co == model_par['co'])[0]

            if not co_index:
                raise ValueError('C/O value not found.')

            co_index = co_index[0]

            flux = flux[teff_index, logg_index, feh_index, co_index, wl_index]

        elif self.model == 'petitcode-hot-cloudy':
            feh = np.asarray(h5_file['models/'+self.model+'/feh'])
            co_ratio = np.asarray(h5_file['models/'+self.model+'/co'])
            fsed_ratio = np.asarray(h5_file['models/'+self.model+'/fsed'])

            teff_index = np.argwhere(teff == model_par['teff'])[0]

            if not teff_index:
                raise ValueError('Temperature value not found.')

            teff_index = teff_index[0]
            logg_index = np.argwhere(logg == model_par['logg'])[0]

            if not logg_index:
                raise ValueError('Surface gravity value not found.')

            logg_index = logg_index[0]
            feh_index = np.argwhere(feh == model_par['feh'])[0]

            if not feh_index:
                raise ValueError('Metallicity value not found.')

            feh_index = feh_index[0]
            co_index = np.argwhere(co == model_par['co'])[0]

            if not co_index:
                raise ValueError('C/O value not found.')

            co_index = co_index[0]
            fsed_index = np.argwhere(fsed == model_par['fsed'])[0]

            if not fsed_index:
                raise ValueError('f_sed value not found.')

            fsed_index = fsed_index[0]

            flux = flux[teff_index, logg_index, feh_index, co_index, fsed_index, wl_index]

        if 'radius' in model_par and 'distance' in model_par:
            scaling = (model_par['radius']*constants.R_JUP)**2 / \
                      (model_par['distance']*constants.PARSEC)**2

            flux *= scaling

        h5_file.close()

        return box.create_box(boxtype='model',
                              model=self.model,
                              wavelength=wl_points,
                              flux=flux,
                              parameters=model_par,
                              quantity='flux')

    def get_photometry(self,
                       model_par,
                       synphot=None):
        """
        Parameters
        ----------
        model_par : dict
            Model parameter values.
        synphot : species.analysis.photometry.SyntheticPhotometry
            Synthetic photometry object.

        Returns
        -------
        float
            Average flux density (W m-2 micron-1).
        """

        if self.spectrum_interp is None:
            self.interpolate()

        spectrum = self.get_model(model_par, None)

        if not synphot:
            synphot = photometry.SyntheticPhotometry(self.filter_name)

        return synphot.spectrum_to_photometry(spectrum.wavelength, spectrum.flux)

    def get_magnitude(self,
                      model_par):
        """
        Parameters
        ----------
        model_par : dict
            Model parameter values.

        Returns
        -------
        float
            Apparent magnitude (mag).
        float
            Absolute magnitude (mag).
        """

        if self.spectrum_interp is None:
            self.interpolate()

        spectrum = self.get_model(model_par, None)
        synphot = photometry.SyntheticPhotometry(self.filter_name)

        if 'distance' in model_par:
            app_mag, abs_mag = synphot.spectrum_to_magnitude(spectrum.wavelength,
                                                             spectrum.flux,
                                                             distance=model_par['distance'])

        else:
            app_mag, abs_mag = synphot.spectrum_to_magnitude(spectrum.wavelength,
                                                             spectrum.flux,
                                                             distance=None)

        return app_mag, abs_mag

    def get_bounds(self):
        """
        Returns
        -------
        dict
            Parameter boundaries of the model grid.
        """

        h5_file = self.open_database()

        teff = h5_file['models/'+self.model+'/teff']
        logg = h5_file['models/'+self.model+'/logg']

        if self.model in ('ames-cond', 'ames-dusty', 'bt-settl'):
            bounds = {'teff': (teff[0], teff[-1]),
                      'logg': (logg[0], logg[-1])}

        elif self.model in ('drift-phoenix', 'bt-nextgen', 'petitcode-cool-clear'):
            feh = h5_file['models/'+self.model+'/feh']

            bounds = {'teff': (teff[0], teff[-1]),
                      'logg': (logg[0], logg[-1]),
                      'feh': (feh[0], feh[-1])}

        elif self.model in ('petitcode-cool-cloudy', ):
            feh = h5_file['models/'+self.model+'/feh']
            fsed = h5_file['models/'+self.model+'/fsed']

            bounds = {'teff': (teff[0], teff[-1]),
                      'logg': (logg[0], logg[-1]),
                      'feh': (feh[0], feh[-1]),
                      'fsed': (fsed[0], fsed[-1])}

        elif self.model in ('petitcode-hot-clear', ):
            feh = h5_file['models/'+self.model+'/feh']
            co_ratio = h5_file['models/'+self.model+'/co']

            bounds = {'teff': (teff[0], teff[-1]),
                      'logg': (logg[0], logg[-1]),
                      'feh': (feh[0], feh[-1]),
                      'co': (co_ratio[0], co_ratio[-1])}

        elif self.model in ('petitcode-hot-cloudy', ):
            feh = h5_file['models/'+self.model+'/feh']
            co_ratio = h5_file['models/'+self.model+'/co']
            fsed = h5_file['models/'+self.model+'/fsed']

            bounds = {'teff': (teff[0], teff[-1]),
                      'logg': (logg[0], logg[-1]),
                      'feh': (feh[0], feh[-1]),
                      'co': (co_ratio[0], co_ratio[-1]),
                      'fsed': (fsed[0], fsed[-1])}

        h5_file.close()

        return bounds

    def get_wavelength(self):
        """
        Returns
        -------
        numpy.ndarray
            Wavelength points (micron).
        """

        h5_file = self.open_database()
        wavelength = np.asarray(h5_file['models/'+self.model+'/wavelength'])
        h5_file.close()

        return wavelength

    def get_points(self):
        """
        Returns
        -------
        dict
            Parameter points of the model grid.
        """

        points = {}

        h5_file = self.open_database()

        teff = h5_file['models/'+self.model+'/teff']
        logg = h5_file['models/'+self.model+'/logg']

        points['teff'] = np.asarray(teff)
        points['logg'] = np.asarray(logg)

        if self.model in ('drift-phoenix', 'bt-nextgen'):
            feh = h5_file['models/'+self.model+'/feh']
            points['feh'] = np.asarray(feh)

        h5_file.close()

        return points

    def get_parameters(self):
        """
        Returns
        -------
        list(str, )
            Model parameters.
        """

        h5_file = self.open_database()

        dset = h5_file['models/'+self.model]
        nparam = dset.attrs['nparam']

        param = []
        for i in range(nparam):
            param.append(dset.attrs['parameter'+str(i)])

        h5_file.close()

        return param
