# ==========================================
# PROJECT: AI MOVIE RECOMMENDER SYSTEM
# DEVELOPER: DARSHAN KOTADIYA
# ROLE: FULL STACK DEVELOPER
# INTERNSHIP: CODSOFT TASK 4
# ==========================================

import streamlit as st
import pandas as pd
import ast
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Page Configuration ---
st.set_page_config(page_title="AI Movie Recommender | Codsoft Task 4", layout="wide")

# --- Helper Function to Clean Data ---
def convert(text):
    """Converts stringified lists from the dataset into Python lists."""
    L = []
    try:
        for i in ast.literal_eval(text):
            L.append(i['name']) 
    except (ValueError, SyntaxError):
        pass
    return L

# --- Load and Process Data ---
@st.cache_resource
def load_data():
    """
    Loads pre-processed data if available, 
    otherwise processes raw CSV files and saves them as pickle files.
    """
    # Check if pre-processed pickle files exist
    if os.path.exists('movies_dict.pkl') and os.path.exists('similarity.pkl'):
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        new_df = pd.DataFrame(movies_dict)
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return new_df, similarity

    # Process raw CSV files from the 'archive' folder
    try:
        movies = pd.read_csv('archive/tmdb_5000_movies.csv')
        credits = pd.read_csv('archive/tmdb_5000_credits.csv')
        
        # Merge datasets on 'title'
        movies = movies.merge(credits, on='title')
        
        # Filter relevant columns
        movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        movies.dropna(inplace=True)
        
        # Clean metadata
        movies['genres'] = movies['genres'].apply(convert)
        movies['keywords'] = movies['keywords'].apply(convert)
        
        # Generate tags for content-based filtering
        movies['tags'] = movies['overview'] + \
                        movies['genres'].apply(lambda x: " ".join(x)) + \
                        movies['keywords'].apply(lambda x: " ".join(x))
        
        new_df = movies[['movie_id', 'title', 'tags']]
        new_df['tags'] = new_df['tags'].apply(lambda x: str(x).lower())
        
        # Vectorization using Scikit-Learn
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(new_df['tags']).toarray()
        similarity = cosine_similarity(vectors)

        # Save processed data for future high-speed loading
        pickle.dump(new_df.to_dict(), open('movies_dict.pkl', 'wb'))
        pickle.dump(similarity, open('similarity.pkl', 'wb'))
        
        return new_df, similarity

    except FileNotFoundError:
        st.error("Dataset not found! Please ensure 'archive' folder contains the TMDB CSV files.")
        return None, None

# --- Recommendation Logic ---
def recommend(movie, df, similarity):
    """Finds the 5 most similar movies based on vector distance."""
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
    st.markdown("---")
    st.subheader("Developed by: Darshan Kotadiya | Full Stack Developer")

    new_df, similarity = load_data()
    
    if new_df is not None:
        # UI Selection
        selected_movie = st.selectbox(
            "Select a movie you liked:",
            new_df['title'].values
        )

        if st.button('Get Recommendations'):
            with st.spinner('Analyzing movie tags...'):
                recommendations = recommend(selected_movie, new_df, similarity)
            
            st.success(f"Because you watched **{selected_movie}**, we recommend:")
            
            # Display Recommendations in columns
            cols = st.columns(5)
            for idx, movie_name in enumerate(recommendations):
                with cols[idx]:
                    st.info(movie_name)

if __name__ == "__main__":
    main()
