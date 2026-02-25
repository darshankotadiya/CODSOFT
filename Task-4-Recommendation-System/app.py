
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
    Loads movies_dict.pkl and calculates similarity matrix live 
    if the large similarity.pkl file is missing.
    """
    try:
        # Check for movies_dict.pkl in your GitHub folder
        # This handles both local and GitHub path structures
        paths = ['Task-4-Recommendation-System/movies_dict.pkl', 'movies_dict.pkl']
        file_path = next((p for p in paths if os.path.exists(p)), None)
        
        if file_path is None:
            st.error("movies_dict.pkl not found! Please ensure it is uploaded to your GitHub folder.")
            return None, None

        # Load the dictionary you already uploaded
        movies_dict = pickle.load(open(file_path, 'rb'))
        new_df = pd.DataFrame(movies_dict)

        # LIVE CALCULATION: 
        # Calculate similarity live on the server since similarity.pkl is too big to upload
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(new_df['tags']).toarray()
        similarity = cosine_similarity(vectors)
        
        return new_df, similarity

    except Exception as e:
        st.error(f"Error loading data: {e}")
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
