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
sect2 = []
sect3 = []
gender = 0
gend = []
y = []
y2 = []
y3 = []
correalation = []
placesDictionary = [(	'ALMUTHANNA',	1	),(	'THIQAR',	2	),(	'KARBALA',	3	),(	'BAGHDAD',	4	), ('KIRKUK',15),(	'NAJAF',	5	),(	'KUT',	6	),(	'NINAWA',	7	),(	'BASRA',	8	),(	'ALMUSAIAB',	9	),(	'MOSUL',	11	),(	'MAYSAN',	12	),(	'NAJAF',	13	),(	'BASRA',	14	),(	'KIRKUK',	15	),(	'HABBANIA',	16	),(	'AMARA',	17	),(	'BAGHDAD',	18	),(	'SALAHUDDIN',	19	),(	'UKLONDON',	20	),(	'ANBAR',	23	),(	'ERBIL',	24	),(	'NINAWA',	25	),(	'WASIT',	27	),(	'NASIRIA',	28	),(	'QADISIA',	29	),(	'TUZKHURMATO',	30	),(	'IRAN',	31	),(	'DUHOK',	33	),(	'TIKRIT',	35	),(	'KARBALA',	36	),(	'THIQAR',	37	),(	'DIYALA',	38	),(	'DIWANIA',	40	),(	'BABIL',	42	),(	'ALMUTHANNA',	43	),(	'DUJAIL',	45	),(	'DUHOKAKRE',	46	),(	'SHIEKHAN',	47	),(	'SINJAR',	49	),(	'SWEDEN',	52	),(	'DOR',	55	),(	'SAMAWA',	56	),(	'KUT',	59	),(	'Sydney',	60	),(	'FALUJA',	61	),(	'INDIANEWDELHI',	62	),(	'BARTILLA',	63	),(	'RAMADI',	64	),(	'SULEYMANIA',	65	),(	'JORDAN',	66	),(	'LEBANON',	67	),(	'SULEYMANIAH',	68	),(	'Akre',	69	),]
PlacesSubstitutions = [('SAMAWA','ALMUTHANNA'),('KUT','WASIT'),('FALUJA','ANBAR'),('HABBANIA','ANBAR'),('RAMADI','ANBAR'),('ALMUSAIAB','BABIL'),('DUHOKAKRE','DUHOK'),('SHIEKHAN','DUHOK'),('INDIANEWDELHI','INDIA'),('AMARA','MAYSAN'),('BARTILLA','NINAWA'),('MOSUL','NINAWA'),('SINJAR','NINAWA'),('DIWANIA','QADISIA'),('DOR','SALAHUDDIN'),('DUJAIL','SALAHUDDIN'),('TUZKHURMATO','SALAHUDDIN'),('SULEYMANIAH','SULEYMANIA'),('UKLONDON','UK'),('KUT','WASIT'), ('AKRE','DUHOK')]
SectGroups = [('Sunni',1),('Shia',2),('Shia major',3),('Sunni',4),('Sunni Major',5),('Non muslim',6)]
AgeGroups = [('12-18',1),('18-25',2),('25-35',3),('35-45',4),('45-65',5),('NA',6)]
with open('d:\Faces_study.csv',mode='r') as csvFile:
    csv_reader = csv.DictReader(csvFile)
    for  vall in csv_reader:
        x = str(vall['ETHNIC RECOG'])
        x2 = str( vall['SECT RECOG'])
        x3 = str(vall['COUNTRY RECOG'])
        if (float(x3) != '0'):
            sect3.append(float(x3))
        if (float(x2) != '0'):
            sect2.append(float(x2))
        if (float(x) != 0):
            sect.append(float(x))
            #print(x)
        #=================== Boolean fields =======================
        #ABORIGINALS_LIVING_THERE
        #ETHNICITY GROUPS DIFFERENCES CTG
        #SECTS AND RELEGIONS DIFFERENCES CTG
        #USA_TV_WORKS
        #EGYPT_TV_WORKS
        #INDIA_TV_WORKS
        #GULF_TV_WORKS
        #IRAN_TV_WORKS
        #TURKEY_TV_WORKS
        #SYRLEBANON_TV_WORKS
        #LATIN_TV_WORKS
        #EAST_ASIAN_WORKS
        #EUROPIAN_TV_WORKS
        #OUTSIDE_IRAQ_5_YEARS
        '''try:
            boolVal = 0
            boolValBefore = str(vall['OUTSIDE_IRAQ_5_YEARS'])
            if boolValBefore == '' :
                continue

            if boolValBefore == 'NO' or boolValBefore == 'FALSE':
                boolVal = 1
            elif boolValBefore == 'YES' or boolValBefore == 'TRUE':
                boolVal = 2
            elif boolValBefore == 'PARTIAL':
                boolVal = 3
            else:
                continue
            if (x != '0'):
                y.append(boolVal)
                sect.append(float(x))

            if (x2 != '0'):
                y2.append(boolVal)
                sect2.append(float(x2))
            if (x3 != '0'):
                y3.append(boolVal)
                sect3.append(float(x3))
        except Exception as e:
            print(e.args)
            continue'''

        #=================== Boolean fields =======================
        # =================== Number Groups =======================
        #IRAQIS RECOGNITION (SELF ASSESSMENT) CTG
        #TOTAL_COUNT
        #LIVED_IN_SOUTH_PROVINCES
        #LIVED_IN_ARABSUNNI_PROVINCES
        #LIVED_IN_SECT_MIXED_PROVINCES
        #LIVED_IN_ETHNIC_MIXED_PROVINCES
        #LIVED_IN_ABORG_POP_PROVINCE
        #LIVED_IN_PURE_KURDISH_AREA
        #LIVED_IN_KURDISH_AREAS2
        #LIVED IN MORE THAN 3 PROV
        #LIVE_IN_MORE_THAN_2_PROVINCES
        #ETHNIC_DIVERSITY
        #SECTARIAN_DIVERSITY
        #SUNNI_ARAB
        #SHIA
        #ABORIGINALS
        #KURDS
        #LIVED_ARAB_CNTRIES
        #LIVED_IN_WEST
        #LIVED_IN_EAST_EUROPE
        #LIVED_ASIA
        #LIVED_INDIA
        #LIVED_NEIGHBR_CNTRIES
        #LIVED_MIDDLEEAST_NARAB
        #LIVED_NORTHAFRICA
        #N_NEIGHBOUR_COUNTRIES_VST
        #N_NGHBR_ARAB_CNTRS_VST
        #N_NGHBR_NONARAB_CNTRS_VST
        '''NG = vall['N_NGHBR_NONARAB_CNTRS_VST']
        if NG == '' or str(NG) == '':
            continue
        NGNumber = 0
        if NG != 'NA':
            NGNumber =  int(NG)
        else:
            continue
        try:
            if (x != '0'):
                y.append(NGNumber)
                sect.append(float(x))

            if (x2 != '0'):
                y2.append(NGNumber)
                sect2.append(float(x2))
            if (x3 != '0'):
                y3.append(NGNumber)
                sect3.append(float(x3))
        except  Exception as e:
            print(e.args)
            continue
        '''
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

sd = np.std(np.array(sect).astype(np.float))
mean = np.mean(np.array(sect).astype(np.float))
print(sd.round(2))
print(mean.round(2))
'''s = pearsonr(sect, y)
s2 = pearsonr(sect2, y2)
s3 = pearsonr(sect3, y3)
print(s3[0].__round__(3))
print(s2[0].__round__(3))
print(s[0].__round__(3))
print(len(y3))
print(len(y2))
print(len(y))
print('\n')
print(s3[1].__round__(3))
print(s2[1].__round__(3))
print(s[1].__round__(3))'''
