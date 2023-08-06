#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import typing as t

from chime_frb_api.core import API

JSON = t.Union[str, int, float, bool, None, t.Mapping[str, "JSON"], t.List["JSON"]]
log = logging.getLogger(__name__)


class Sources(object):
    """
    CHIME/FRB Sources API

    Parameters
    ----------
    API : chime_frb_api.core.API class-type

    Returns
    -------
    object-type
    """

    def __init__(self, API: API):
        self.API = API

    def get_source(self, source_name: str) -> JSON:
        """
        Astrophysical Source from CHIME/FRB Master

        Parameters
        ----------
        source_name : str
            Source name, e.g. CAS_A

        Returns
        -------
        source : dict
        """
        assert source_name, AttributeError("source_name is required")
        return self.API.get("/v1/sources/{}".format(source_name))

    def get_expected_spectrum(self, source_name: str) -> JSON:
        """
        Expected spectra for a CHIME/FRB Source

        Parameters
        ----------
        source_name : str
            Source name, e.g. CAS_A

        Returns
        -------
        spectrum : dict
            Returns dict with the following format
            {"freqs": [], "expected_spectrum": []}
        """
        assert source_name, AttributeError("source_name is required")
        return self.API.get("/v1/sources/spectrum/{}".format(source_name))
