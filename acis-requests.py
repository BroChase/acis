import urllib3
import numpy as np
import regex as re
import json
import pandas as pd


def getRange(start, end, FIPS):
    base_url = 'http://data.rcc-acis.org/MultiStnData'
    http = urllib3.PoolManager()
    params = {
        "county": FIPS,
        "sdate": start,
        "edate": end,
        "elems": "pcpn,avgt"
    }
    r = http.request('GET', base_url, fields=params)
    p = json.loads(r.data.decode('utf-8'))
    preciplist = []
    templist = []
    for i, data in p.items():
        for m in data:
            df = pd.DataFrame(m['data'])
            ser = df.to_dict()
            for k, value in ser.items():
                if k == 0:
                    preciplist.append(value)
                else:
                    templist.append(value)

    df = pd.DataFrame(preciplist)
    df2 = pd.DataFrame(templist)
    # replace missing M variables with zeros
    df.replace('M', np.nan, inplace=True)
    df2.replace('M', np.nan, inplace=True)

    df.replace('S', np.nan, inplace=True)
    df2.replace('S', np.nan, inplace=True)
    # replace missing T variables with zeros
    df.replace('T', np.nan, inplace=True)
    df2.replace('T', np.nan, inplace=True)

    df.replace(['A', '\*'], value='0', regex=True, inplace=True)
    df2.replace(['A', '\*'], value='0', regex=True, inplace=True)


    avg = []
    avg2 =[]
    # find the regions average precipitation per day
    for i in range(df.shape[1]):
        df[i] = df[i].astype('float64')
        nantotal = df[i].isnull().sum()
        total = df[i].sum()
        avg.append(total/(df.shape[0]-nantotal))
    for i in range(df2.shape[1]):
        df2[i] = df2[i].astype('float64')
        nantotal = df2[i].isnull().sum()
        total = df2[i].sum()
        avg2.append(total/(df.shape[0]-nantotal))
    return avg, avg2


# '08113', '08091', '08111', '08067', '08053', '08079','08109', '08049', '08037', '08051','08065', '08097', '08117',
# '08107', '08057', '08069', '08013'
FIPS_ids = ['08019']

for c in FIPS_ids:
    L1 = []
    L2 = []
    FIPS = c
    sdate = 1990
    for i in range(26):
        startdate = str(sdate+i) + '-1-1'
        enddate = str(sdate+i) + '-12-31'
        Plist, Tlist = getRange(startdate, enddate, FIPS)
        L1.append(Plist)
        L2.append(Tlist)


    df = pd.DataFrame.from_records(L1)
    df2 = pd.DataFrame.from_records(L2)
    df.to_csv(FIPS+'precip.csv')
    df2.to_csv(FIPS+'temp.csv')