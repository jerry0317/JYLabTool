from .jyldata import JYLData

# import methods.manage as clm
from ..methods import manage as clm

class JYLDataPoint(object):
    def __init__(self, fromList=None):
        super(JYLDataPoint, self).__init__()
        self.data = []
        if fromList is not None:
            self.fromList(fromList)

    # data = []

    def _checkSingularity(self):
        nameList = [d.name for d in self.data]
        nSet = clm.verifySingularity(names=nameList, returnSet=True, exception=True, exceptionText="The data names in this data point is not singular.")
        return nSet

    @property
    def dataNames(self):
        nSet = self._checkSingularity()
        return nSet

    @dataNames.setter
    def dataNames(self, value):
        oldNames = self.dataNames
        for name in value:
            if name not in oldNames:
                self.data.append(JYLData(name=name))
        self._checkSingularity()

    @property
    def attr(self):
        dic = {}
        for d in self.data:
            dic[d.name] = d
        return dic

    @property
    def valueDict(self):
        dic = {}
        for d in self.data:
            dic[d.name] = d.value
        return dic

    @property
    def uncertaintyDict(self):
        dic = {}
        for d in self.data:
            dic[d.name] = d.uncertainty
        return dic

    @property
    def unitDict(self):
        dic = {}
        for d in self.data:
            dic[d.name] = d.unit
        return dic

    def setValue(self, attr, value):
        self.attr[attr].value = value

    def setUnit(self, attr, unit):
        self.attr[attr].unit = unit

    def setUncertainty(self, attr, uncertainty):
        self.attr[attr].uncertainty = uncertainty

    def fromList(self, li):
        for l in li:
            d = JYLData(name=l["name"], value=l["value"], unit=l["unit"], uncertainty=l["uncertainty"])
            self.data.append(d)
