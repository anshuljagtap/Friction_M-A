import streamlit as st
import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to connect to SQLite database and fetch data
def get_data(table_name):
    connection = sqlite3.connect('database.db')
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

# Function to calculate similarity between buyer and seller goals
def calculate_similarity(buyer_goals, seller_goals):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([buyer_goals, seller_goals])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

# Function to find matches for a buyer
def find_matches(buyer, sellers):
    matches = []
    for _, seller in sellers.iterrows():
        if buyer['industry'] == seller['industry']:
            similarity = calculate_similarity(buyer['goals'], seller['goals'])
            if similarity > 0.5:
                matches.append((seller['name'], similarity))
    return sorted(matches, key=lambda x: x[1], reverse=True)

# Streamlit App
st.title("Intelligent M&A Deal Matcher")

# Sidebar for adding new profiles
st.sidebar.header("Input New Profile")
with st.sidebar:
    option = st.selectbox("Add Profile To:", ["Buyers", "Sellers"])
    name = st.text_input("Name")
    industry = st.text_input("Industry")
    revenue = st.number_input("Revenue", min_value=0)
    goals = st.text_area("Goals")
    if st.button("Submit"):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO {option.lower()} (name, industry, revenue, goals) VALUES (?, ?, ?, ?)",
            (name, industry, revenue, goals),
        )
        connection.commit()
        connection.close()
        st.success(f"{name} added to {option} database!")

# Display Matches
st.header("Buyer-Seller Matches")
buyers = get_data("buyers")
sellers = get_data("sellers")

for _, buyer in buyers.iterrows():
    st.subheader(f"Buyer: {buyer['name']} ({buyer['industry']})")
    matches = find_matches(buyer, sellers)
    if matches:
        for match in matches:
            st.write(f"- **{match[0]}** (Similarity: {match[1]:.2f})")
    else:
        st.write("No matches found.")
