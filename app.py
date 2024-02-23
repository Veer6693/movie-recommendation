import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl','rb'))
CS = pickle.load(open('CS.pkl','rb'))

movies_name = movies['title'].values

def recommend_movie(movie_name):

    recommend = []
    movie_poster = []

    index = movies[movies['title'] == movie_name].index[0]
    movies_list = sorted(list(enumerate(CS[index])),reverse=True,key= lambda x : x[1])[1:6]
    for title in movies_list:
        recommend.append(movies.iloc[title[0]].title)
        url = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2edcd964476e4c9dc9a5f644cb29b841&language=en-US".format(movies.iloc[title[0]].movie_id))
        data = url.json()
        poster_url = "https://image.tmdb.org/t/p/original/"+data['poster_path']
        movie_poster.append(poster_url)



    return recommend, movie_poster


st.title("Movie Recommendation")

movie = st.selectbox('Select a movie', movies_name)


if st.button('Recommend'):

    recommended_movie, movie_poster = recommend_movie(movie)

    cols = st.columns(len(recommended_movie))
    
    for i in range(len(recommended_movie)):
        cols[i].write(recommended_movie[i])
        cols[i].image(movie_poster[i])
