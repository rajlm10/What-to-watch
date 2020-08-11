# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df1=pd.read_csv('movies.csv')
df2=pd.read_csv('ratings.csv')

data=pd.merge(df1,df2,on='movieId')

data.describe()

ratings = pd.DataFrame(data.groupby('title')['rating'].mean()).reset_index()
ratings.head()
temp = pd.DataFrame(data.groupby('title')['rating'].count()).reset_index()
temp=temp.drop(['title'],axis=1)
ratings['number_of_ratings']=temp
ratings.head()

movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
movie_matrix.head()

ratings.sort_values('number_of_ratings', ascending=False).head(75)

movie_user_rating = movie_matrix['Up (2009)']


similar_to_movie=movie_matrix.corrwith(movie_user_rating)


corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation']).reset_index()


series=pd.Series(ratings['number_of_ratings'],name='number_of_ratings')

corr_movie = corr_movie.join(series)

recommended=corr_movie[corr_movie['number_of_ratings'] >=75].sort_values(by='Correlation', ascending=False).head(10)

tp = data.pivot_table(index='userId', columns='title', values='rating',fill_value=0)

tp=tp.to_numpy()