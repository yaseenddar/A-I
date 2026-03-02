import streamlit as st
import pandas as pd
import preprocess
import helper
import os

# ----------------------------
# Load Data
# ----------------------------

data_dir = os.path.join(os.path.dirname(__file__), 'data')

df = pd.read_csv(os.path.join(data_dir, 'athlete_events.csv'))
region_df = pd.read_csv(os.path.join(data_dir, 'noc_regions.csv'))

# Preprocess
df_processed = preprocess.preprocess_data(df, region_df)

# ----------------------------
# Sidebar Filters
# ----------------------------

st.sidebar.title("Filters")

user_input = st.sidebar.radio(
    "Select Analysis Type",
    ["Medal Tally", "Overall Analysis", "Country-wise Analysis", "Athlete-wise Analysis"]
)

years = ["Overall"] + sorted(df_processed['Year'].unique().tolist())[::-1]
year = st.sidebar.selectbox("Select Year", years)

countries = ["Overall"] + sorted(df_processed["region"].dropna().unique().tolist())
country = st.sidebar.selectbox("Select Country", countries)

# ----------------------------
# Apply Filters
# ----------------------------

df_filtered = helper.filter_data(df_processed, year, country)

# ----------------------------
# Dynamic Title
# ----------------------------

st.title(helper.generate_title(year, country))

# ----------------------------
# Page Logic
# ----------------------------

if user_input == "Medal Tally":
    medal_data = helper.medal_tally(df_filtered)
    st.dataframe(medal_data)

elif user_input == "Overall Analysis":
    st.dataframe(df_filtered)

elif user_input == "Country-wise Analysis":
    top_10 = helper.top_10_countries(df_filtered)
    st.subheader("Top 10 Countries")
    st.dataframe(top_10)

elif user_input == "Athlete-wise Analysis":
    st.write("Feature coming soon 🚀")