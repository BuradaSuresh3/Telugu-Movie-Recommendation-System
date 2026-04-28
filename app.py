import streamlit as st
import pandas as pd

# Load dataset
movies = pd.read_csv("dataset/telugu_movies_2021_2026_50_plus.csv")

st.title("🎬 Telugu Movie Recommendation System")

st.subheader("Search by Genre")

# Genre dropdown
genres = sorted(movies["Genre/Type"].unique())

selected_genre = st.selectbox(
    "Select Genre",
    genres
)

# Filter movies by selected genre
filtered_movies = movies[
    movies["Genre/Type"].str.contains(selected_genre, case=False)
]

if st.button("Show Recommended Movies"):
    st.subheader(f"Top Movies in {selected_genre}")

    for _, row in filtered_movies.iterrows():
        st.write(
            f"🎥 {row['Movie Name']} | ⭐ {row['Rating']} | 👤 {row['Hero']}"
        )