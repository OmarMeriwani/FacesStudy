import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
import seaborn

df  =pd.read_csv('D:\FINAL_SET_FACES.csv', header=0, sep=',')
Y = df.values[:,47]
X = df.values[:,0:54]
X_std = StandardScaler().fit_transform(X)


pca = PCA(n_components=30)
pca.fit(X_std,y=Y)
X_pca=pca.transform(X_std)

ex_variance=np.var(X_pca,axis=0)
ex_variance_ratio = ex_variance/np.sum(ex_variance)
print (ex_variance_ratio)

plt.figure(figsize = (30,30))
features=list(df.columns[47:54])# select the 'worst' features
s=seaborn.heatmap(df[features].corr(),cmap='coolwarm',annot=True, linewidths=.5)
s.set_yticklabels(s.get_yticklabels(),rotation=30,fontsize=30)
s.set_xticklabels(s.get_xticklabels(),rotation=30,fontsize=30)
plt.savefig('heatmap2.png')


#print(X_PCA)
#principalDf = pd.DataFrame(data = principalComponents, columns=['PCA1','PCA2'])
#finalDf = pd.concat([principalDf, Y], axis = 1)

'''
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'PCA1']
               , finalDf.loc[indicesToKeep, 'PCA2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
'''
