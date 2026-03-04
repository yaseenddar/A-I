import preprocess
import pandas as pd
import streamlit as st

def medal_tally(df):
    # Keep only rows with medals
    df = df[df['Medal'].notna()].copy()

    # Remove duplicate team medals
    df = df.drop_duplicates(
        subset=["NOC","Year","Games","Event","Sport","Medal"]
    )
    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]
    # Aggregate by region and year
    medal_tally = (
        df.groupby(['region', 'Year'])[['Gold','Silver','Bronze','Total']]
        .sum()
        .sort_values(by=['Year'], ascending=False)
        .reset_index()
    )

    return medal_tally

def generate_title(user_input, year, country):
    if user_input == "Medal Tally":
        if year == "Overall" and country == "Overall":
            return "Overall Olympic Medal Tally"
        elif year != "Overall" and country == "Overall":
            return f"Olympics {year} - Medal Tally"
        elif year == "Overall" and country != "Overall":
            return f"{country} - Overall Medal Tally"
        else:
            return f"{country} - {year} Medal Tally"
    elif user_input == "Overall Analysis":
        if year == "Overall" and country == "Overall":
            return "Overall Olympic Analysis"
        elif year != "Overall" and country == "Overall":
            return f"Olympics {year} - All Countries Analysis"
        elif year == "Overall" and country != "Overall":
            return f"{country} - Overall Performance Analysis"
        else:
            return f"{country} - {year} Performance Analysis"


        return f"{country} - Overall Performance"
    else:
        return f"{country} - {year} Performance"

def filter_data(df, year, country):
    df_filtered = df.copy()

    if year != "Overall":
        df_filtered = df_filtered[df_filtered["Year"] == int(year)]

    if country != "Overall":
        df_filtered = df_filtered[df_filtered["region"] == country]

    return df_filtered

# dynamic data in Event based 
def event_based_data(df,col,colName):
     return(
        df
        .groupby('Year')[col]
        .nunique()
        .reset_index(name=colName)
        .sort_values('Year')
         )