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

    # Add total column
    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]

    # Aggregate
    medal_tally = (
        df.groupby('region')[['Gold','Silver','Bronze','Total']]
        .sum()
        .sort_values(by=['Gold','Silver','Bronze'], ascending=False)
        .reset_index()
    )

    return medal_tally
def medal_tally(df):
    df = df[df['Medal'].notna()].copy()

    df = df.drop_duplicates(
        subset=["NOC","Year","Games","Event","Sport","Medal"]
    )

    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]

    medal_tally = (
        df.groupby('region')[['Gold','Silver','Bronze','Total']]
        .sum()
        .sort_values(by=['Gold','Silver','Bronze'], ascending=False)
        .reset_index()
    )

    return medal_tally

def generate_title(year, country):
    if year == "Overall" and country == "Overall":
        return "Overall Olympic Analysis"
    elif year != "Overall" and country == "Overall":
        return f"Olympics {year} - All Countries"
    elif year == "Overall" and country != "Overall":
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