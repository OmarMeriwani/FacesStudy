import pandas as pd
import numpy as np
#from sklearn import datasets, linear_model
#from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from sklearn import datasets
import sklearn
import rpy2
from rpy2 import robjects as ro
from scipy.stats.stats import pearsonr
from difflib import SequenceMatcher

import csv
sectrecog = 0
sect = []
gender = 0
gend = []
y = []
correalation = []
placesDictionary = [(	'ALMUTHANNA',	1	),(	'THIQAR',	2	),(	'KARBALA',	3	),(	'BAGHDAD',	4	), ('KIRKUK',15),(	'NAJAF',	5	),(	'KUT',	6	),(	'NINAWA',	7	),(	'BASRA',	8	),(	'ALMUSAIAB',	9	),(	'MOSUL',	11	),(	'MAYSAN',	12	),(	'NAJAF',	13	),(	'BASRA',	14	),(	'KIRKUK',	15	),(	'HABBANIA',	16	),(	'AMARA',	17	),(	'BAGHDAD',	18	),(	'SALAHUDDIN',	19	),(	'UKLONDON',	20	),(	'ANBAR',	23	),(	'ERBIL',	24	),(	'NINAWA',	25	),(	'WASIT',	27	),(	'NASIRIA',	28	),(	'QADISIA',	29	),(	'TUZKHURMATO',	30	),(	'IRAN',	31	),(	'DUHOK',	33	),(	'TIKRIT',	35	),(	'KARBALA',	36	),(	'THIQAR',	37	),(	'DIYALA',	38	),(	'DIWANIA',	40	),(	'BABIL',	42	),(	'ALMUTHANNA',	43	),(	'DUJAIL',	45	),(	'DUHOKAKRE',	46	),(	'SHIEKHAN',	47	),(	'SINJAR',	49	),(	'SWEDEN',	52	),(	'DOR',	55	),(	'SAMAWA',	56	),(	'KUT',	59	),(	'Sydney',	60	),(	'FALUJA',	61	),(	'INDIANEWDELHI',	62	),(	'BARTILLA',	63	),(	'RAMADI',	64	),(	'SULEYMANIA',	65	),(	'JORDAN',	66	),(	'LEBANON',	67	),(	'SULEYMANIAH',	68	),(	'Akre',	69	),]
PlacesSubstitutions = [('SAMAWA','ALMUTHANNA'),('KUT','WASIT'),('FALUJA','ANBAR'),('HABBANIA','ANBAR'),('RAMADI','ANBAR'),('ALMUSAIAB','BABIL'),('DUHOKAKRE','DUHOK'),('SHIEKHAN','DUHOK'),('INDIANEWDELHI','INDIA'),('AMARA','MAYSAN'),('BARTILLA','NINAWA'),('MOSUL','NINAWA'),('SINJAR','NINAWA'),('DIWANIA','QADISIA'),('DOR','SALAHUDDIN'),('DUJAIL','SALAHUDDIN'),('TUZKHURMATO','SALAHUDDIN'),('SULEYMANIAH','SULEYMANIA'),('UKLONDON','UK'),('KUT','WASIT'), ('AKRE','DUHOK')]
print(type(placesDictionary))
with open('d:\Faces_study.csv',mode='r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for  vall in csv_reader:
        x = vall['SECT RECOG']
        yy = vall['WHERE DO YOU LIVE NOW']
        yyval = 0

        if (x == '#DIV/0!'):
            continue
        if (x == '0'):
            continue
        try:
            sect.append(float(x))
        except Exception as e:
            continue
        for t in PlacesSubstitutions:
            if str(yy).lower() == t[0].lower()  :
                yy = t[1]
                #print(t[0], ':', yy)
        for item in placesDictionary:
            if str(item[0]).lower() == yy.lower() \
                or (SequenceMatcher(None, item[0].lower(), str(yy).lower()).ratio() > 0.7) \
                   or (str(item[0]).lower() in yy.lower()) \
                   or (yy.lower() in str(item[0]).lower())                :
                yyval = item[1]
                y.append(yyval)
                break

        if yyval == 0:
            y.append(0)
        #if (yyval == 0):
            #print(yyval, ':', yy)
print(len(y), ':', len(sect))
'''a = []
for x in gend:
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
gend = a
a = []
for x in sect:
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
    a.append(x)
sect = a'''
s = pearsonr(sect, y)
print('Correlation coefficient: ', s[0].__round__(3))
print('P-Value: ', s[1].__round__(3))
#correlationval = ro.r.cor(csv_reader, method='pearson')