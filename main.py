import pickle
import streamlit as st
import requests
import json
import http.client
import time

def movie_details(movie_name):
    url = "https://movie-details1.p.rapidapi.com/imdb_api/movie"
    querystring = {"id": iddd(movie_name)}
    headers = {
        "X-RapidAPI-Host": "movie-details1.p.rapidapi.com",
        "X-RapidAPI-Key": "472a6d2210msh03124957d5c6fb5p1ceaf8jsn281b03a656d2"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    val = response.json()
    rating=val['rating']
    release_year=val['release_year']
    duration=val['runtime']
    description=val['description']
    actors=val['actors']
    return rating,release_year,duration,description,actors

def iddd(movie_name):
    url = "https://online-movie-database.p.rapidapi.com/auto-complete"
    print(movie_name)
    querystring = {"q": movie_name}
    headers = {
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com",
        "X-RapidAPI-Key": "472a6d2210msh03124957d5c6fb5p1ceaf8jsn281b03a656d2"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    val=response.json()
    i=val["d"][0]["id"]
    return i


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    genre = data['genres']
    data_genre = []
    for x in genre:
        data_genre.append(x['name'])
        # print(x['name'])
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path,data_genre

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_genre = []

    with st.spinner('Bear with me ...'):
        for i in distances[1:12]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            a,b=fetch_poster(movie_id)
            recommended_movie_posters.append(a)
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_genre.append(b)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_genre


st.header('Sinemate')
movies = pickle.load(open('models/movie_list.pkl','rb'))
similarity = pickle.load(open('models/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_genre = recommend(selected_movie)

    # Row 1
    st.subheader(recommended_movie_names[0])
    st.image(recommended_movie_posters[0],width=250,caption=recommended_movie_names[0])
    print('\n')
    y=''
    for x in recommended_movie_genre[0]:
        y+=x+' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[0])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads=''
        for i in range(0,4):
            leads+=actors[i]['name']+' , '
        st.markdown("Cast : " + str(leads))


    # Row 2:
    st.subheader(recommended_movie_names[1])
    st.image(recommended_movie_posters[1],width=250,caption=recommended_movie_names[1])
    print('\n')
    y = ''
    for x in recommended_movie_genre[1]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[1])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # ROW 3:
    st.subheader(recommended_movie_names[2])
    st.image(recommended_movie_posters[2],width=250,caption=recommended_movie_names[2])
    print('\n')
    y = ''
    for x in recommended_movie_genre[2]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[2])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # Row 4
    st.subheader(recommended_movie_names[3])
    st.image(recommended_movie_posters[3], width=250, caption=recommended_movie_names[3])
    print('\n')
    y = ''
    for x in recommended_movie_genre[3]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[3])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # Row 5
    st.subheader(recommended_movie_names[4])
    st.image(recommended_movie_posters[4],width=250,caption=recommended_movie_names[4])
    print('\n')
    y = ''
    for x in recommended_movie_genre[4]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[4])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # ROW 6
    st.subheader(recommended_movie_names[5])
    st.image(recommended_movie_posters[5], width=250, caption=recommended_movie_names[5])
    print('\n')
    y = ''
    for x in recommended_movie_genre[5]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[5])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # Row 7
    st.subheader(recommended_movie_names[6])
    st.image(recommended_movie_posters[6], width=250, caption=recommended_movie_names[6])
    print('\n')
    y = ''
    for x in recommended_movie_genre[6]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[6])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # Row 8
    st.subheader(recommended_movie_names[7])
    st.image(recommended_movie_posters[7], width=250, caption=recommended_movie_names[7])
    print('\n')
    y = ''
    for x in recommended_movie_genre[7]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[7])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))


    # Row 9
    st.subheader(recommended_movie_names[8])
    st.image(recommended_movie_posters[8], width=250, caption=recommended_movie_names[8])
    print('\n')
    y = ''
    for x in recommended_movie_genre[8]:
        y += x + ' , '
    with st.spinner('Fetching movie details ...'):
        rating, release_year, duration, description, actors = movie_details(recommended_movie_names[8])
        st.markdown("Ratings : " + str(rating))
        st.markdown("Release Year : " + str(release_year))
        st.markdown("Duration : " + str(duration))
        st.markdown("Genre : " + y)
        st.markdown("Description : " + str(description))
        leads = ''
        for i in range(0, 4):
            leads += actors[i]['name'] + ' , '
        st.markdown("Cast : " + str(leads))

