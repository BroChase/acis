import urllib3
import numpy as np
import regex as re
import json
import pandas as pd
import os


def getRange(start, end, FIPS):

    # url for acis multiyear data
    base_url = 'http://data.rcc-acis.org/MultiStnData'
    http = urllib3.PoolManager()
    params = {
        "county": FIPS,
        "sdate": start,
        "edate": end,
        "elems": "pcpn,avgt"
    }
    # request the data GET
    r = http.request('GET', base_url, fields=params)
    # decode the json
    p = json.loads(r.data.decode('utf-8'))
    # to hold precipitation
    preciplist = []
    # to hold temperatures
    templist = []
    # iterate the items in the json to extract the precipitations and temps
    for i, data in p.items():
        for m in data:
            df = pd.DataFrame(m['data'])
            ser = df.to_dict()
            for k, value in ser.items():
                if k == 0:
                    preciplist.append(value)
                else:
                    templist.append(value)
    # create a dataframe from the precipitation and one for the temps
    df = pd.DataFrame(preciplist)
    df2 = pd.DataFrame(templist)
    # replace missing M'missing' variables with zeros
    df.replace('M', np.nan, inplace=True)
    df2.replace('M', np.nan, inplace=True)
    # replace S'sparse' variables with zeros
    df.replace('S', np.nan, inplace=True)
    df2.replace('S', np.nan, inplace=True)
    # replace missing T'trace' variables with zeros
    df.replace('T', np.nan, inplace=True)
    df2.replace('T', np.nan, inplace=True)
    # replace A 'appended' leap year variable
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


def multi_year_data(FIPS_ids, startdate, years):
    for c in FIPS_ids:
        # L1= list for precipitation row=a year columns=average per day 365 days
        L1 = []
        # L2= list for temps row= a year columns= average per day 365 days
        L2 = []
        FIPS = c
        sdate = startdate
        for i in range(years):
            startdate = str(sdate + i) + '-1-1'
            enddate = str(sdate + i) + '-12-31'
            Plist, Tlist = getRange(startdate, enddate, FIPS)
            L1.append(Plist)
            L2.append(Tlist)

        df = pd.DataFrame.from_records(L1)
        df2 = pd.DataFrame.from_records(L2)
        makedir(startdate+'/precip')
        makedir(startdate+'/temp')
        df.to_csv(startdate+'/precip/' + FIPS + 'precip.csv')
        df2.to_csv(startdate+'/temp/' + FIPS + 'temp.csv')


def single_year_data(FIPS_ids):

    for c in FIPS_ids:
        FIPS = c
        L1 = []
        L2 = []
        startdate = '2017-1-1'
        enddate = '2017-12-31'
        Plist, Tlist = getRange(startdate, enddate, FIPS)
        L1.append(Plist)
        L2.append(Tlist)

        df = pd.DataFrame.from_records(L1)
        df2 = pd.DataFrame.from_records(L2)
        makedir(startdate+'/precip')
        makedir(startdate+'/temp')
        df.to_csv(startdate+'/precip/' + FIPS + 'precip.csv')
        df2.to_csv(startdate+'/temp/' + FIPS + 'temp.csv')


def makedir(path):
    if os.path.isdir(path): pass
    elif os.path.isfile(path):
        raise OSError("%s exists." % path)
    else:
        parent, directory = os.path.split(path)
        if parent and not os.path.isdir(parent): makedir(parent)
        if directory: os.mkdir(path)