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
SectGroups = [('Sunni',1),('Shia',2),('Shia major',3),('Sunni',4),('Sunni Major',5),('Non muslim',6)]
AgeGroups = [('12-18',1),('18-25',2),('25-35',3),('35-45',4),('45-65',5),('NA',6)]
with open('d:\Faces_study.csv',mode='r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for  vall in csv_reader:
        x = vall['ETHNIC RECOG']
        if (x == '#DIV/0!'):
            continue
        if (x == '0'):
            continue
        #=================== Boolean fields =======================
        #ABORIGINALS_LIVING_THERE
        '''try:
            boolVal = 0
            boolValBefore = str(vall['ABORIGINALS_LIVING_THERE'])
            #print(boolValBefore)
            if boolValBefore == '' :
                continue

            if boolValBefore == 'NO':
                boolVal = 1
            elif boolValBefore == 'YES':
                boolVal = 2

            y.append(boolVal)
            sect.append(float(x))
        except Exception as e:
            print(e.args)
            continue'''

        #=================== Boolean fields =======================
        # =================== Number Groups =======================
        NG = vall['IRAQIS RECOGNITION (SELF ASSESSMENT) CTG']
        if NG == '' or str(NG) == '':
            continue
        NGNumber = 0
        if NG != 'NA':
            NGNumber =  int(NG)
        else:
            continue
        try:
            y.append(NGNumber)
            sect.append(float(x))
        except  Exception as e:
            print(e.args)
            continue

        # =================== Number Groups =======================
        # =================== Age Groups =======================
        '''if vall['AGE'] == '' or str(vall['AGE']) == '':
            continue

        for item in AgeGroups:
            try:
                if str(item[0]).lower() == str(vall['AGE']).lower():
                    print(item[0])
                    try:
                        y.append( item[1])
                        sect.append(float(x))
                    except:
                        continue
                    break
            except  Exception as e:
                print(e.args)'''

        # =================== Age Groups =======================
        #=================== Living & Origin Place Sect =======================
        '''if vall['ORIGIN CITY SECT'] == '' or str(vall['ORIGIN CITY SECT']) == '':
            continue

        for item in SectGroups:
            try:
                if str(item[0]).lower() == str(vall['ORIGIN CITY SECT']).lower():
                    print(item[0])
                    try:
                        y.append( item[1])
                        sect.append(float(x))
                    except:
                        continue
                    break
            except  Exception as e:
                print(e.args)'''

        #=================== Living & Origin Place Sect =======================

        #=================== Living Place  & ORIGIN CITY =======================
        '''yy = vall['ORIGIN CITY']
        yyval = 0
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
            y.append(0)'''
        #=================== Living Place End ======================
print(len(y), ':', len(sect))
s = pearsonr(sect, y)
print('Correlation coefficient: ', s[0].__round__(3))
print('P-Value: ', s[1].__round__(3))
