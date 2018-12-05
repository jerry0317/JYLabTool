#!/usr/bin/env python3

import JYL
import JYL.plot as jplt
import JYL.methods.filem as jflm

import numpy as np

# x = JYL.JYLDataPoint()
#
# x.dataNames = ["mass", "length", "length"]
#
# x.setValue("length", 0.5)
#
# # print(x.dataNames)
# # print([d.name for d in x.data])
# print(x.valueDict["length"])

s = JYL.JYLDataSet()

xList = list(np.random.randint(0,100,size=10))
yList = list(np.random.randint(0,100,size=10))
xuList = list(np.random.randint(0,5,size=10))
yuList = list(np.random.randint(0,20,size=10))

for i in range(0,10):
    dicX = {"name": "x", "value": xList[i], "unit": "g", "uncertainty": xuList[i]}
    dicY = {"name": "y", "value": yList[i], "unit": "m", "uncertainty": yuList[i]}
    dp = JYL.JYLDataPoint(fromList=[dicX, dicY])
    s.addDataPoint(dp)

# print([len(dp.data) for dp in s.dataPoints])
# print([(dp.valueDict["x"], dp.valueDict["y"]) for dp in s.dataPoints])

# jplt.twoWayPlot(s, "x", "y")

s2 = jflm.openFromCSV(path="sT.csv")
# print([(dp.valueDict["x"], dp.valueDict["y"]) for dp in s2.dataPoints])
jplt.twoWayPlot(s2, "x", "y")
