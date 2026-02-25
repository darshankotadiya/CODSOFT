import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Page Configuration ---
st.set_page_config(page_title="Movie Recommender | Codsoft Task 4", layout="wide")

# --- Function to Clean Data ---
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L

# --- Load and Process Data ---
@st.cache_resource
def load_data():
    # Load files from the 'archive' folder as seen in your VS Code
    movies = pd.read_csv('archive/tmdb_5000_movies.csv')
    credits = pd.read_csv('archive/tmdb_5000_credits.csv')
    
    # Merge datasets on 'title'
    movies = movies.merge(credits, on='title')
    
    # Selecting relevant columns for content-based filtering
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
    movies.dropna(inplace=True)
    
    # Preprocessing genres and keywords
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    
    # Create tags
    movies['tags'] = movies['overview'] + str(movies['genres']) + str(movies['keywords'])
    new_df = movies[['movie_id', 'title', 'tags']]
    new_df['tags'] = new_df['tags'].apply(lambda x: str(x).lower())
    
    return new_df

# --- Recommendation Logic ---
def recommend(movie, df, similarity):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies

# --- Main Streamlit App ---
def main():
    st.title("🎬 AI-Powered Movie Recommender")
    st.subheader("Developed by: Darshan Kotadiya | Full Stack Developer")

    try:
        new_df = load_data()
        
        # Vectorization
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(new_df['tags']).toarray()
        similarity = cosine_similarity(vectors)

        # UI for selection
        selected_movie = st.selectbox(
            "Which movie did you watch recently?",
            new_df['title'].values
        )

        if st.button('Get Recommendations'):
            recommendations = recommend(selected_movie, new_df, similarity)
            st.success(f"Because you liked **{selected_movie}**, you might also enjoy:")
            
            # Displaying recommendations
            cols = st.columns(5)
            for idx, movie in enumerate(recommendations):
                with cols[idx]:
                    st.info(movie)

    except FileNotFoundError:
        st.error("Error: Could not find dataset files in the 'archive' folder.")

if __name__ == "__main__":
    main()
