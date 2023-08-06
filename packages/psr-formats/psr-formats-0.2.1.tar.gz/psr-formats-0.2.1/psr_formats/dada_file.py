# dada_file.py
import logging
import os
import datetime

import numpy as np
import astropy.units as u

from .data_file import DataFile
from .util import (
    load_dada_file,
    dump_dada_file
)

module_logger = logging.getLogger(__name__)


class DADAFile(DataFile):

    default_header = {
        "HDR_VERSION": "1.0",
        "HDR_SIZE": "4096",
        "TELESCOPE": "PKS",
        "PRIMARY": "dspsr",
        "UTC_START": "2007-05-18-15:55:58",
        "SOURCE": "J1644-4559",
        "RA": "16:44:49.28",
        "DEC": "-45:59:09.5",
        "FREQ": "1405.000000",
        "BW": "40",
        "TSAMP": "0.0125",
        "NBIT": "32",
        "NDIM": "2",
        "NPOL": "2",
        "NCHAN": "1",
        "MODE": "PSR",
        "OBS_OFFSET": "0",
        "INSTRUMENT": "dspsr",
        "DSB": "0",
        "PFB_DC_CHAN": "1"
    }

    timestamp_formatter = "%Y-%m-%d-%H:%M:%S"

    def __init__(self, file_path: str):
        super(DADAFile, self).__init__(file_path)
        self._header = self.default_header.copy()
        self.logger = module_logger.getChild("DADAFile")

    def _load_data_from_file(self) -> None:

        self._header, self._data = load_dada_file(self.file_path)

    def _shape_data(self, data: np.ndarray) -> None:

        if self._header is None:
            raise RuntimeError(("DADAFile._shape_data: Need to load "
                                "data from file before calling _shape_data"))

        ndim, nchan, npol = [int(self[item])
                             for item in ["NDIM", "NCHAN", "NPOL"]]

        data = data.reshape((-1, nchan, npol, ndim))
        if ndim == 2:  # means we're dealing with complex data
            data = data[:, :, :, 0] + 1j*data[:, :, :, 1]
        elif ndim == 1:
            data = data[:, :, :, 0]

        return data

    @property
    def utc_start(self) -> datetime.datetime:
        return datetime.datetime.strptime(
            self._header["UTC_START"], self.timestamp_formatter)

    @utc_start.setter
    def utc_start(self, new_utc_start):
        """
        Can either pass a str or a datetime object.
        If str doesn't fit `timestamp_formatter` class attribute,
        then raises ValueError
        """
        if hasattr(new_utc_start, "strftime"):  # passing datetime object
            self._header["UTC_START"] = new_utc_start.strftime(
                self.timestamp_formatter)
        else:  # passing str object
            datetime.datetime.strptime(
                new_utc_start, self.timestamp_formatter)
            self._header["UTC_START"] = new_utc_start

    def load_data(self):
        self._loaded = True
        self._load_data_from_file()
        self._data = self._shape_data(self._data).copy()
        return self

    def dump_data(self, overwrite: bool = True) -> str:

        new_file_path = self.file_path
        if not overwrite:
            exists = os.path.exists(new_file_path)
            temp_file_path = new_file_path
            # temp_file_path = f"{new_file_path}.{i}"
            i = 0
            while exists:
                temp_file_path = f"{new_file_path}.{i}"
                exists = os.path.exists(temp_file_path)
                i += 1
            new_file_path = temp_file_path

        if self.ndim == 1:
            data = self.data.flatten()
        else:
            dtype = np.float32 if self.nbit == 32 else np.float64
            data = np.zeros((self.ndat, self.nchan, self.ndim*self.npol),
                            dtype=dtype)
            for pol in range(self.npol):
                data[:, :, pol*2] = self.data[:, :, pol].real
                data[:, :, pol*2 + 1] = self.data[:, :, pol].imag
        self.logger.debug(f"dump_data: new file path: {new_file_path}")
        dump_dada_file(new_file_path, self.header, data)
        return new_file_path


def _add_properties(cls: type, properties: dict) -> type:

    def prop_factory(
        prop_name: str,
        header_name: str,
        unit: u.Quantity
    ) -> property:

        def fget(obj):
            return float(obj[header_name]) * unit

        def fset(obj, new_value):
            if hasattr(new_value, "value"):
                obj[header_name] = str(f"{new_value.to(unit).value:.6f}")
            else:
                obj[header_name] = str(new_value)

        return property(fget, fset)

    for prop_name in properties:
        prop = properties[prop_name]
        header_name, unit = prop["header_name"], prop["unit"]
        setattr(cls, prop_name, prop_factory(prop_name, header_name, unit))

    return cls


_properties = {
    "bw": {
        "header_name": "BW",
        "unit": u.MHz
    },
    "centre_frequency": {
        "header_name": "FREQ",
        "unit": u.MHz
    },
    "sampling_rate": {
        "header_name": "TSAMP",
        "unit": u.us
    }
}

DADAFile = _add_properties(DADAFile, _properties)
