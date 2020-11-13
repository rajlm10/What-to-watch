# Importing the libraries
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



X=np.random.randn(nm,100)*0.01
Theta=np.random.randn(nu,100)*0.01




def cost_function(X,Theta,Y,R):
    Xtheta=(np.dot(X,Theta.T))*R
    
    Xc=Xtheta[Xtheta!=0]
    Yc=Y[Y!=0]
    cost=round(0.5*(np.power((Xc-Yc),2).sum()),2)
    return cost
    

def compute_gradients(X,Theta,Y,R):
    dX=np.zeros(X.shape)
    dTheta=np.zeros(Theta.shape)
    dX=np.dot(R*(np.dot(X,Theta.T)-Y),Theta)
    dTheta=np.dot((R*(np.dot(X,Theta.T)-Y)).T,X)
    return dX,dTheta


def gradient_descent(X,Theta,Y,R,iterations,alpha):
    for i in range(iterations):
        
        cost=cost_function(X,Theta,Y,R)
        dX,dTheta=compute_gradients(X,Theta,Y,R)
        X=X-(alpha*dX)
        Theta=Theta-(alpha*dTheta)
        print(cost)
    return X,Theta


Xtrained,Thetatrained=gradient_descent(X,Theta,Y,R,5000,6*1e-4)

import pickle
pickle.dump([Xtrained,Thetatrained], open("trial.p", "wb"))



