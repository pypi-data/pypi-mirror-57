# basics
import json
import re
# for stats
import numpy as np
import pandas as pd
from scipy import stats
import requests


def getItem(item):
    if type(item).__name__ not in ["int", "float"]:
        return item.item()
    else:
        return item


def getStats(data):
    try:
        jsonData = {}

        dataCount = len(data)

        # About the data
        jsonData["dataType"] = str(data.dtypes)
        jsonData["dataCount"] = dataCount
        jsonData["dataUnique"] = len(data.unique())

        # Basic stats
        jsonData["mean"] = data.mean()
        jsonData["median"] = data.median()
        jsonData["std"] = data.std()
        jsonData["mode"] = data.mode().values.tolist()[0]

        minV = data.min()
        maxV = data.max()
        minV = getItem(minV)
        maxV = getItem(maxV)

        jsonData["minV"] = minV
        jsonData["maxV"] = maxV

        # # BoxPlot
        q1 = data.quantile(.25)
        q3 = data.quantile(.75)
        irq = q3-q1

        jsonData["q1"] = q1
        jsonData["q3"] = q3
        jsonData["irq"] = irq

        # # Find wiskis borders min/max
        def findMin(a, b): return a if (a > b) else b

        def findMax(a, b): return a if (a < b) else b

        # # Find edges
        minBox = q1-1.5*irq
        maxBox = q3+1.5*irq
        minBox = findMin(minBox, minV)
        maxBox = findMax(maxBox, maxV)
        jsonData["minBox"] = getItem(minBox)
        jsonData["maxBox"] = getItem(maxBox)

        # # ANOMALIES
        # # find outliers
        maxOut = data[data > maxBox].count()
        minOut = data[data < minBox].count()

        maxOut = getItem(maxOut)
        minOut = getItem(minOut)

        jsonData["maxOut"] = maxOut
        jsonData["minOut"] = minOut
        jsonData["maxOutPerc"] = maxOut/dataCount
        jsonData["minOutPerc"] = minOut/dataCount

        # # Count NaNs and Inf
        Nans = np.isnan(data).sum().item()
        jsonData["Nans"] = Nans
        jsonData["NansPerc"] = Nans/dataCount
        Infs = np.isinf(data).sum().item()
        jsonData["Infs"] = Infs
        jsonData["InfsPerc"] = Infs/dataCount

        return jsonData
    except:
        return 0


def GetNumericalDisrt(data, binSize):
    data = data[~data.isin([np.nan, np.inf, -np.inf])]
    try:
        distr = np.histogram(data, bins=binSize)
        x = distr[1].tolist()
        y = distr[0]/distr[0].sum()  # normilized
        y = y.tolist()
        y_orig = distr[0]
        y_orig = y_orig.tolist()
        return x, y, y_orig
    except:
        return [], [], []


def GetCatorigicalDisrt(data):
    data = data[~data.isin([np.nan, np.inf, -np.inf])]
    try:
        categorical = data.value_counts()
        categorical_norm = categorical/categorical.sum()
        x = categorical.keys().to_list()  # tricky conversion
        y = categorical_norm.values.tolist()
        y_orig = categorical.values.tolist()
        return x, y, y_orig
    except:
        return [], [], []


def cleanColumn(data):
        # check if the type is right
    allowedDataTypes = ["int",	"int_", "int8", "int16", "int32", "int64", "uint8",
                        "uint16", "uint32", "uint64", "float",	"float_", "float16", "float32", "float64"]
    # if not numerical, try to convert
    if data.dtypes not in allowedDataTypes:
        try:
            # try to convert to numerical
            data = pd.to_numeric(data, errors='coerce', downcast='signed')
            if data.dtypes in allowedDataTypes:
                origSize = data.size
                data = data.dropna()
                numericalSize = data.size
                return data, origSize, numericalSize
            else:
                return 0, 0, 0
        except:
            return 0, 0, 0
    else:
        # if nomerical, all good, p just continue with the data
        dataCount = data.size
        return data, dataCount, dataCount


def schema(df, name):
    colNames = df.columns
    # define main json dict
    JSON_main = {}
    # to filter out the ones that were skipped
    newColNames = []

    for i in colNames:
        mycolumn = df[i]
        # clean the dataset here
        mycolumn, origSize, numericalSize = cleanColumn(mycolumn)
        # if the data not numerical and cannot be converted, skip it
        if type(mycolumn) is pd.Series:  # checking agains pandas type. not sure if the best way
                # jsonData = getStatsJSON(mycolumn)
            jsonData = getStats(mycolumn)

            if jsonData == 0:
                continue

            # add the data about non numerical vals
            nonNumeric = origSize - numericalSize
            nonNumericPerc = nonNumeric/origSize
            jsonData["nonNumeric"] = nonNumeric
            jsonData["nonNumericPerc"] = nonNumericPerc

            if type(jsonData) == dict:
                # only keep colnames of numerical data
                newColNames.append(i)

                JSON_main[i] = {"Descr": {},
                                "Distr": {"x": [], "y": []}}
                JSON_main[i]["Descr"] = jsonData

                # if many unique vals, limit histogram to 100 bins
                if jsonData["dataUnique"] > 99:
                    x_distr, y_disrt, y_orig_disrt = GetNumericalDisrt(
                        mycolumn, 100)
                elif jsonData["dataUnique"] > 19:
                    x_distr, y_disrt, y_orig_disrt = GetNumericalDisrt(
                        mycolumn, jsonData["dataUnique"])
                else:
                    x_distr, y_disrt, y_orig_disrt = GetCatorigicalDisrt(
                        mycolumn)
                JSON_main[i]["Distr"]["x"] = x_distr
                JSON_main[i]["Distr"]["y"] = y_disrt
                JSON_main[i]["Distr"]["y_orig"] = y_orig_disrt
            else:
                print("not numerical...")
                continue
        else:
            print("not continuing")
            continue
    JSON_main['colNames'] = newColNames
    return JSON_main


def upload(JSONdict, key):
    JSONdict["key"] = key
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    try:
        r = requests.post('http://3.224.141.181:5000/upload',
                          json=JSONdict, headers=headers)
        if r.status_code == 200:
            print(
                f"Great! you can see your data here: http://3.224.141.181:3000/view/{json.loads(r.content)['PID']}")
        else:
            print(json.loads(r.content)['result'])
    except:
        print("something is wrong...")
