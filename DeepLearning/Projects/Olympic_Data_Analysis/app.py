import streamlit as st
import pandas as pd
import preprocess
import helper
import os
import plotly.express as px
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

st.title(helper.generate_title(user_input, year, country))
st.subheader(f" - Total Medals: {df_filtered['Medal'].notna().sum()}")

# ----------------------------
# Page Logic
# ----------------------------
if user_input == "Medal Tally":
    medal_data = helper.medal_tally(df_filtered)
    st.dataframe(medal_data)

elif user_input == "Overall Analysis":
    #  make column wise count unique analysis cities years events sports
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        cities =df['City'].unique().shape[0]
        st.subheader(f"Number of Cities: {cities}")

    with col2:
        years = df['Year'].unique().shape[0]
        st.subheader(f"Number of Years: {years}")

    with col3:
        events = df['Event'].unique().shape[0]
        st.subheader(f"Number of Events: {events}")
 
    with col1:
        sports = df['Sport'].unique().shape[0]
        st.subheader(f"Number of Sports: {sports}")

    # clo1, clo2 = st.columns(2)
    with col2:
        # number of nations participated over the years
        nations = df_filtered['region'].unique().shape[0]
        st.subheader(f"Number of Nations: {nations}")
    st.dataframe(df_filtered)
    with col3:
        # number of athelets over the years        
        athletes_over_years = df_filtered["Name"].unique().shape[0]
        st.subheader("Number of Athletes over the years")
        st.subheader(f"{athletes_over_years}")
        
        # Number of Atheletes in every Event Year Wise 
    year_wise_athlete_count = helper.event_based_data(df_filtered,'Name','Atheletes');
    fig = px.line(year_wise_athlete_count,x='Year',y="Atheletes" )
    st.plotly_chart(fig) 

    #  Nombe of Sports Events in Event
    year_wise_sports_count = helper.event_based_data(df_filtered,'Sport','Sports')
    fig = px.line(year_wise_sports_count,x='Year',y='Sports') 
    st.plotly_chart(fig)


elif user_input == "Country-wise Analysis":
    top_10 = helper.top_10_countries(df_filtered)
    st.subheader("Top 10 Countries")
    st.dataframe(top_10)


    # graph

elif user_input == "Athlete-wise Analysis":
    st.write("Feature coming soon 🚀")