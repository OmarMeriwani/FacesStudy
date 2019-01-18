import pandas as pd
import numpy as np
from scipy import stats
from sklearn.feature_selection import SelectKBest, f_classif, f_regression
from sklearn.feature_selection import chi2
from scipy.stats.stats import pearsonr


df  =pd.read_csv('D:\FINAL_SET_FACES.csv', header=0, sep=',')
df  =pd.read_csv('D:\FINAL_SET_FACES_SECT.csv', header=0, sep=',')
df  =pd.read_csv('D:\FINAL_SET_FACES_TOTAL.csv', header=0, sep=',')
df  =pd.read_csv('D:\FINAL_SET_FACES_ETHNIC.csv', header=0, sep=',')

Y = df.values[:,53]
sd = np.std(np.array(Y).astype(np.float))
mean = np.mean(np.array(Y).astype(np.float))
print(sd.round(2))
print(mean.round(2))

for i in range(1,47):
    s3 = pearsonr(df.values[:,i], Y)
    print(df.columns.values[i], ';',s3[0].__round__(3),';' ,s3[1].__round__(3))
