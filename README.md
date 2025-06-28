🍽️ Swiggy’s Restaurant Recommendation System using Streamlit
📌 Project Overview
This project presents a restaurant recommendation system inspired by Swiggy, designed using Python, Pandas, Scikit-learn, and Streamlit. The system allows users to input preferences like city, cuisine, rating, and cost to receive personalized restaurant suggestions using Cosine Similarity on encoded restaurant features.

✅ Features
🔎 User Input Panel for city, cuisine, rating, and price filters.

🧠 Machine Learning-based Recommendation using Cosine Similarity.

📊 Interactive UI built with Streamlit.

💡 Efficient handling of high-cardinality categorical data using optimized One-Hot Encoding.

📄 Exported files:

cleaned_data.csv: Cleaned restaurant dataset.

encoded_data.csv: One-Hot Encoded data.

encoder.pkl: Saved encoder for future transformation.

🔧 Tech Stack
Frontend: Streamlit

Backend: Python

Libraries: pandas, numpy, scikit-learn, streamlit, pickle

Recommendation Algorithm: Cosine Similarity

🧼 Data Cleaning (Step 1)
Removed duplicates and irrelevant columns like 'license'.

Replaced invalid ratings like '--' with NaN.

Converted rating, rating_count, and cost to numeric.

Removed rows with missing critical values.

Saved the cleaned data as cleaned_data.csv.

🔄 Data Preprocessing (Step 2)
Applied One-Hot Encoding on categorical features: name, city, cuisine.

Saved encoder object as encoder.pkl.

Ensured all columns in encoded data were numeric.

Output stored as encoded_data.csv.

🧠 Recommendation Methodology (Step 3)
Used Cosine Similarity to compute similarity between restaurants based on encoded features.

Mapped similar restaurants from the encoded dataset to the original cleaned data.

Ensured performance with optimized column selection to prevent MemoryError.

🖥️ Streamlit Application (Step 4)
Sidebar for user preferences (city, cuisine, rating, max cost).

Restaurant filter and recommendation based on a selected restaurant.

Displays top 5 similar restaurants using cosine similarity.

Enhanced UI with set_page_config, emojis, and markdown.

🚀 How to Run
bash
Copy
Edit
# Step 1: Clone the repository
git clone https://github.com/Bhuvanesh-432/Mini_Project_Four.git
cd swiggy-recommendation-app

# Step 2: Install requirements
pip install -r requirements.txt

# Step 3: Run the Streamlit app
streamlit run app.py
📂 Folder Structure
bash
Copy
Edit
swiggy-recommendation-app/
├── app.py                  # Streamlit Application
├── cleaned_data.csv        # Cleaned restaurant data
├── encoded_data.csv        # One-Hot encoded dataset
├── encoder.pkl             # Saved OneHotEncoder object
├── README.md               # Project Documentation
├── requirements.txt        # Python dependencies
❤️ Built With
Love for Swiggy

Power of Streamlit

Simplicity of Python

Backed by AI & ML

📧 Contact
For queries or suggestions:
📮 Email: bhuvanesh20g013@gmil.com
🌐 GitHub: github.com/Bhuvanesh-432
