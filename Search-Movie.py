import streamlit as st
import requests
from nltk.tokenize import word_tokenize

nltk.download("punkt")

st.set_page_config(page_title='SEARCH | MOVIE', page_icon='favicon.png')
#https://www.omdbapi.com/?apikey=YOUR_API_KEY&type=actor&s={actor_name}
st.header("Search Movie")

def fetch_img(actor):
    url = f"https://api.themoviedb.org/3/search/person?api_key=80157c67e91cf936a7c0f4675704beb6&query={actor}"
    response = requests.get(url)
    data = response.json()

    # Check if the response contains any results
    if data["total_results"] > 0:
        # Extract the image URL of the first result
        first_result = data["results"][0]
        profile_path = first_result["profile_path"]

        if profile_path:
            # Build the complete image URL using the profile_path
            base_url = "https://image.tmdb.org/t/p/w500"
            image_url = base_url + profile_path

        return image_url

movie = st.text_input("Enter A Movie Name")
movie = movie.lower()   
movie = word_tokenize(movie)
movie = " ".join(movie)

if st.button("Search"):
    try:
        url = f'https://www.omdbapi.com/?apikey=f4e281ed&t={movie}'
        r = requests.get(url)
        data = r.json()
        
        col1, col2 = st.columns(2)
        col5, col6, col7 = st.columns(3)

        with col1:
            st.image(data['Poster'], width=350)
        
        with col2:
            st.header(data['Title'])
            st.write(f"###### {data['Released']} {data['Genre']} {data['Runtime']} {data['Rated']}")
            st.write(f"#### User Ratings - {data['Ratings'][0]['Value']}")
            st.write("##### Overview")
            st.write(data['Plot'] + " with awards of " + data['Awards'] + " of " + data['Country'] + " in languages - " + data['Language'] )
            col3, col4 = st.columns(2)

            with col3:
                st.write(f"##### Director")
                st.write(data['Director'])

            with col4:
                st.write(f"##### Writer")
                st.write(data['Writer'])

            actors = data['Actors']
            actors = actors.split(', ')

            st.markdown("\n")
            st.markdown("\n")
            st.markdown("\n")

            st.header("Star Cast")

            with col5:
                try:
                    first = (fetch_img(actors[0]))
                    st.image(first)
                    st.write(f"#### {actors[0]}")
                except:
                    st.write("### Image Not Available")

            
            with col6:
                try:
                    second = (fetch_img(actors[1]))
                    st.image(second)
                    st.write(f"#### {actors[1]}")
                except:
                    st.write("### Image Not Available")
            
            
            with col7:
                try:
                    third = (fetch_img(actors[2]))
                    st.image(third)
                    st.write(f"#### {actors[2]}")
                except:
                    st.write("### Image Not Available")

    except:
        st.write("### Unable To Find Infromation About This Film Please Check The Movie Name")
            

            


    

