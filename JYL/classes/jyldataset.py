# import methods.manage as clm
from ..methods import manage as clm
from .jyldatapoint import JYLDataPoint

class JYLDataSet(object):
    def __init__(self):
        self.dataPoints = []
        super(JYLDataSet, self).__init__()

    # dataPoints = []

    def _checkNameSingularity(self):
        nSets = [dp.dataNames for dp in self.dataPoints]
        v = clm.verifyEqualityOfSets(nSets, returnSet=True)
        if v is False:
            raise Exception("The data points have different data names.")
        else:
            return v

    @property
    def dataNames(self):
        nSet = self._checkNameSingularity()
        return nSet

    def addDataPoint(self, dp):
        self.dataPoints.append(dp)

    @property
    def values(self):
        dic = {}
        for n in self.dataNames:
            dic[n] = [dp.valueDict[n] for dp in self.dataPoints]
        return dic

    @property
    def uncertainties(self):
        dic = {}
        for n in self.dataNames:
            dic[n] = [dp.uncertaintyDict[n] for dp in self.dataPoints]
        return dic

    @property
    def units(self):
        dic = {}
        for n in self.dataNames:
            dic[n] = [dp.unitDict[n] for dp in self.dataPoints]
        return dic

    @property
    def acsList(self):
        bl = []
        for dp in self.dataPoints:
            dic = {}
            for d in dp.data:
                dic[d.name] = {"value": d.value, "uncertainty": d.uncertainty, "unit": d.unit}
            bl.append(dic)
        return bl

    @property
    def length(self):
        return len(self.dataPoints)
