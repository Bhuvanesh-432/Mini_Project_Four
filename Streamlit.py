import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# --- Page Configuration ---
st.set_page_config(
    page_title="Swiggy Restaurant Recommender",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Data ---
@st.cache_data
def load_data():
    cleaned_df = pd.read_csv("cleaned_data.csv")
    encoded_df = pd.read_csv("encoded_data.csv")
    with open("encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    return cleaned_df, encoded_df, encoder

cleaned_df, encoded_df, encoder = load_data()

# --- Sidebar: Filters ---
st.sidebar.header("🔍 Filter Restaurants")

# City and Cuisine Filters
cities = sorted(cleaned_df['city'].dropna().unique())
cuisines = sorted(set(c.strip() for sublist in cleaned_df['cuisine'].dropna().str.split(",") for c in sublist))

selected_city = st.sidebar.selectbox("City", cities)
selected_cuisines = st.sidebar.multiselect("Preferred Cuisines", cuisines)
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.5, step=0.1)
max_cost = st.sidebar.number_input("Maximum Cost for Two (₹)", min_value=0, value=500)
num_recommendations = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# --- Filter Dataset Based on Input ---
filtered_df = cleaned_df[
    (cleaned_df['city'] == selected_city) &
    (cleaned_df['rating'] >= min_rating) &
    (cleaned_df['cost'] <= max_cost) &
    (cleaned_df['cuisine'].apply(lambda x: any(cuisine in x for cuisine in selected_cuisines)))
]

st.title("🍽️ Swiggy Restaurant Recommendation System")
st.markdown("Discover restaurants based on your preferences and get similar recommendations!")

if filtered_df.empty:
    st.warning("❗ No restaurants found with the selected filters.")
else:
    st.success(f"✅ Found {len(filtered_df)} restaurants in {selected_city}.")

    # --- Restaurant Selection ---
    selected_restaurant = st.selectbox("Select a Restaurant to Find Similar Ones", filtered_df['name'].unique())

    if st.button("🔎 Show Similar Restaurants"):
        try:
            # Locate selected restaurant uniquely using name + city
            selected_row = cleaned_df[
                (cleaned_df['name'] == selected_restaurant) &
                (cleaned_df['city'] == selected_city)
            ]

            if selected_row.empty:
                st.error("Selected restaurant not found in main dataset.")
            else:
                index = selected_row.index[0]
                similarity_scores = cosine_similarity([encoded_df.iloc[index]], encoded_df)[0]

                similar_indices = similarity_scores.argsort()[::-1][1:num_recommendations+1]
                recommended = cleaned_df.iloc[similar_indices][['name', 'city', 'rating', 'cuisine', 'cost']]

                if recommended.empty:
                    st.info("No similar restaurants found.")
                else:
                    st.subheader("🍴 Top Similar Restaurants")
                    st.dataframe(recommended.reset_index(drop=True))
        except Exception as e:
            st.error(f"Error in generating recommendations: {e}")

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 10px; font-size: 16px;'>
        Made with ❤️ using <strong>Swiggy Data</strong> and <strong>Streamlit</strong> <br>
        <small>© 2025 | Restaurant Recommendation System</small>
    </div>
    """,
    unsafe_allow_html=True
)

