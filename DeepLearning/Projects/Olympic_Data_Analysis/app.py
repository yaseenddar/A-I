import streamlit as st
import pandas as pd
import preprocess
import helper
import os
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
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
    copied_df = df_filtered.copy()
    year_wise_athlete_count = helper.event_based_data(df_processed,'NOC','Countries');
    fig = px.line(year_wise_athlete_count,x='Year',y="Countries" )
    st.plotly_chart(fig) 

    #  Nombe of Sports Events in Event
    year_wise_sports_count = helper.event_based_data(df_processed,'Sport','Sports')
    fig = px.line(year_wise_sports_count,x='Year',y='Sports') 
    st.plotly_chart(fig)

    # Age wise eprobablity
    # Age wise probability distribution
    # age_data = df_filtered["Age"].dropna()

    # fig2 = ff.create_distplot(
    # [age_data],                  # ✅ list of arrays
    # ['Age Distribution'],
    # show_hist=False,
    # show_rug=False
    # )
    # st.plotly_chart(fig2.show())  

    # pribability distribution 
    df_filtered = df_filtered.drop_duplicates(subset=['Name','region'])
    age_data = df_filtered["Age"].dropna()
    gold_age_wise = df_filtered[df_filtered["Medal"] == "Gold"]["Age"].dropna()
    silver_age_wise = df_filtered[df_filtered["Medal"] == "Silver"]["Age"].dropna()
    bronze_age_wise = df_filtered[df_filtered["Medal"] == "Bronze"]["Age"].dropna()
    weight_data = df_filtered[df_filtered["Weight"] > 70 ]["Age"].dropna()
    fig2 = ff.create_distplot(
    [age_data,gold_age_wise,silver_age_wise,bronze_age_wise,weight_data],                  # ✅ list of arrays
    ['Age Distribution','Gold Analysis','Silver Analysis','Bronze Analysis','Weight Analysis'],
    show_hist=False,
    show_rug=False
    )
    st.plotly_chart(fig2)

elif user_input == "Country-wise Analysis":
    # country_list = ["Overall"] + sorted(df_processed["region"].dropna().unique().tolist())
    # country = st.sidebar.selectbox("Select Country", country_list)  # ✅ defined here

    st.title(f"{country} Analysis")                                  # ✅ f-string

    copied_df = df_filtered.copy()                                  # ✅ use df_processed, not df_filtered

    year_wise_medal_count = helper.country_based_data(copied_df, country)  # ✅ pass country

    st.dataframe(year_wise_medal_count)                       # ✅ show result, not raw df_filtered
    st.subheader(country+" Year/Medal-Analysis")
    fig = px.line(year_wise_medal_count, x="Year", y="Total")
    st.plotly_chart(fig)
  
    # heatmap for the country

    st.subheader("HeatMap of ",country+"data")
    result = helper.country_wise_data(copied_df,country)

    fig, ax = plt.subplots(figsize=(20, 15))     # ✅ control width x height


    sns.heatmap(result,annot=True)
    st.pyplot(fig)

    # graph

elif user_input == "Athlete-wise Analysis":
    sportList = ["Overall"] + sorted(df_filtered["Sport"].dropna().unique().tolist())
    sport = st.selectbox("Select Sport", sportList)
    st.title("TOP 10 Athletes in ",sport)
    if sport:
        new_data= helper.top_10_data(df_filtered,sport)
        st.table(new_data)

    # Gold per sport with age distribution
    famous_sport = df_filtered["Sport"].unique().tolist()

    x = []
    labels = []
    for sport in famous_sport:
        ages = df_filtered[df_filtered["Sport"] == sport]["Age"].dropna()
        if len(ages) >= 2:  # Only include sports with at least 2 age values for KDE
            x.append(ages)
            labels.append(sport)
    
    if x:  # Only create plot if there are valid datasets
        fig2 = ff.create_distplot(
        x,
        labels,
        show_hist=False,
        show_rug=False
        )
        st.plotly_chart(fig2)
    else:
        st.write("Not enough data to create distribution plot.")