from ..classes.jyldata import JYLData
from ..classes.jyldataset import JYLDataSet
from ..classes.jyldatapoint import JYLDataPoint

import csv


def saveToCSV(dataset, path=None, file=None):
    header = []
    for n in dataset.dataNames:
        header.extend(["{}_value".format(n), "{}_uncertainty".format(n), "{}_unit".format(n)])
    if path is not None:
        csvFile = open(path, "w")
    if file is not None:
        csvFile = file

    dict_writer = csv.DictWriter(csvFile, header)

    dict_writer.writeheader()

    for dp in dataset.dataPoints:
        dict = {}
        for n in dataset.dataNames:
            dict["{}_value".format(n)] = dp.valueDict[n]
            dict["{}_uncertainty".format(n)] = dp.uncertaintyDict[n]
            dict["{}_unit".format(n)] = dp.unitDict[n]
        dict_writer.writerow(dict)

    csvFile.close()

def openFromCSV(path=None, file=None):

    if path is not None:
        csvFile = open(path, "r")
    if file is not None:
        csvFile = file

    dict_reader = csv.DictReader(csvFile,skipinitialspace=True)

    di = {}
    for h in dict_reader.fieldnames:
        hs = h.rsplit("_", 1)
        pre = hs[0]
        suf = hs[1]
        if pre not in di:
            di[pre] = set([suf])
        else:
            di[pre].add(suf)

    zSet = set(["value", "uncertainty", "unit"])

    for k, v in di.items():
        if v != zSet:
            raise Exception("The format of CSV file is incorrect.")

    names = di.keys()

    s = JYLDataSet()

    for row in dict_reader:
        li = []
        for n in names:
            dic = {}
            dic["name"] = n
            dic["value"] = float(row["{}_value".format(n)])
            dic["uncertainty"] = float(row["{}_uncertainty".format(n)])
            dic["unit"] = row["{}_unit".format(n)]
            li.append(dic)
        dp = JYLDataPoint(fromList=li)
        s.dataPoints.append(dp)

    return s
