#!/usr/bin/env python3

# import methods.manage as clm
from ..methods import manage as clm

class JYLData(object):
    def __init__(self, name=None, value=None, uncertainty=None, unit=None):
        super(JYLData, self).__init__()
        self.name = ""
        self.value = 0.0
        self.uncertainty = 0.0
        self.unit = ""
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if uncertainty is not None:
            self.uncertainty = uncertainty
        if unit is not None:
            self.unit = unit

    # name = ""
    # value = 0.0
    # uncertainty = 0.0
    # unit = ""
