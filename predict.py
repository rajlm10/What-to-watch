import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1=pd.read_csv('movies.csv')
df2=pd.read_csv('ratings.csv')

data=pd.merge(df1,df2,on='movieId')
data=data.drop(['genres','timestamp'],axis=1)
data.describe()

data.loc[100836]=[1]+["Toy Story (1995)"]+[611]+[5]
data.loc[100837]=[318]+["Shawshank Redemption, The (1994)"]+[611]+[5]
data.loc[100838]=[47099]+["Pursuit of Happyness, The (2006)"]+[611]+[5]
data.loc[100839]=[3578]+["Gladiator (2000)"]+[611]+[3.5]
data.loc[100840]=[73881]+["3 Idiots (2009)"]+[611]+[5]
data.loc[100841]=[103042]+["Man of Steel (2013)"]+[611]+[3]
data.loc[100842]=[2411]+["Rocky IV (1985)"]+[611]+[4]
data.loc[100843]=[88140]+["Captain America: The First Avenger (2011)"]+[611]+[4]
data.loc[100844]=[103688]+["Conjuring, The (2013)"]+[611]+[4.5]
data.loc[100845]=[106782]+["Wolf of Wall Street, The (2013)"]+[611]+[5]




ratings = pd.DataFrame(data.groupby('title')['rating'].mean()).reset_index()
ratings.head()
temp = pd.DataFrame(data.groupby('title')['rating'].count()).reset_index()
temp=temp.drop(['title'],axis=1)
ratings['number_of_ratings']=temp
ratings.head()

Y = data.pivot_table(index=['userId'], columns=['title'], values='rating',fill_value=0)
 
columns=list(Y.columns)

Y=Y.to_numpy()


R = data.pivot_table(index='userId', columns='title', values='rating',fill_value=0)
R[R != 0] = 1

R=R.to_numpy()

Y=Y.T
R=R.T

nm=9719
nu=612



Xtrained,Thetatrained = pickle.load(open("trial.p","rb"))

Ypredict=np.dot(Xtrained,Thetatrained.T)

Ypredict=Ypredict.T

Raj=Ypredict[610]

RR=[]

for s in range(9719):
    if Raj[s]>=4.85:
        print(columns[s])
    

   


