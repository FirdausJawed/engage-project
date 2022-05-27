import pickle
import streamlit as st
import requests

# genre lang rate sorting
def movie_rating_wise(genre, lang, rate, sorting):
    url = "https://ott-details.p.rapidapi.com/advancedsearch"

    querystring = {"start_year": "1970", "end_year": "2022", "min_imdb": str(rate), "max_imdb": "10", "genre": str(genre),
                   "language": str(lang), "type": "movie", "sort": str(sorting), "page": "1"}
    headers = {
        "X-RapidAPI-Host": "ott-details.p.rapidapi.com",
        "X-RapidAPI-Key": "472a6d2210msh03124957d5c6fb5p1ceaf8jsn281b03a656d2"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    val = response.json()
    now = val['results']
    return now

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

    with st.spinner('Wait for a few seconds ...'):
        for i in distances[1:12]:
            # fetch the movie poster
            movie_id = movies.iloc[i[0]].movie_id
            a,b=fetch_poster(movie_id)
            recommended_movie_posters.append(a)
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_genre.append(b)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_genre

selected_option= st.sidebar.selectbox(
        "Select the type of recommendation system you want :",
        ( 'Genre', 'Movie'))

if selected_option=="Movie":

    st.header('Sinemate as Movie Recommendation System')
    movies = pickle.load(open('models/movie_list.pkl','rb'))
    similarity = pickle.load(open('models/similarity.pkl','rb'))


    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names,recommended_movie_posters,recommended_movie_genre = recommend(selected_movie)

        # Rows
        for i in range(0,9):
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i],width=250,caption=recommended_movie_names[i])
            print('\n')
            y=''
            for x in recommended_movie_genre[i]:
                y+=x+' , '
            with st.spinner('Fetching movie details ...'):
                rating, release_year, duration, description, actors = movie_details(recommended_movie_names[i])
                st.markdown("Ratings : " + str(rating))
                st.markdown("Release Year : " + str(release_year))
                st.markdown("Duration : " + str(duration))
                st.markdown("Genre : " + y)
                st.markdown("Description : " + str(description))
                leads=''
                for j in range(0,4):
                    leads+=actors[j]['name']+' , '
                st.markdown("Cast : " + str(leads))

elif selected_option=="Genre":
    st.header("Sinemate as Genre Based Recommendation System")
    genre = st.selectbox(
        "Select the genre form the drop down",
        ('action','Comedy','romance', 'Drama', 'Documentary','horror','drama','thriller'))

    lang = st.radio(
        "Please Select the language of the film",
        ('English', 'Hindi', 'Tamil','French','Japanese'))

    rate = st.slider('Select the minimum rating of the movie ', 0, 10, 1)

    sorting = st.selectbox(
        'Select the order of filtering?',
        ('highestrated' , 'lowestrated' , 'latest' , 'oldest'))

    if st.button('Show Recommendation'):
        with st.spinner('Fetching movie details ...'):
            val=movie_rating_wise(genre ,lang ,rate ,sorting)


        for i in range(0,len(val)):
            st.subheader(val[i]['title'])
            try:
                st.image(val[i]['imageurl'],caption=val[i]["title"])
            except:
                print("Image Not found")
            st.markdown("Ratings : " + str(val[i]['imdbrating']))
            st.markdown("Release Year : " + str(val[i]['released']))
            try:
                st.markdown("Genre : " + str(val[i]['genre'][0]))
            except:
                print("Ratings Not found")
            st.markdown("Description : " + str(val[i]['synopsis']))