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
def country_based_data(final_df, country, colName=''):
   final_df["Total"] = final_df["Gold"] + final_df["Silver"] + final_df["Bronze"]
   country_df = final_df.groupby(['region',"Year"])[["Total"]].sum().sort_values(by='Year',ascending=True).reset_index()
   if country == "Overall":
       return country_df
   else:
       return country_df[country_df['region'] == country]

def top_10_data(final_df,sport):
    # add total column
    final_df["Total"] = final_df["Gold"] + final_df["Silver"] + final_df["Bronze"]
    final_df.dropna(subset='Medal')
    # Step 1: Rank all countries by total medals
    new_df = (
        final_df.groupby('Name')[["Total"]]
        .sum()
        .sort_values(by="Total", ascending=False)
        .reset_index()
    )

    # Step 2: Merge, then break down by Sport — keep both Gold and Total
    result = (
        final_df.merge(new_df["Name"], on="Name")          # bring in top context
        .groupby(["Name", "Sport","NOC"])[["Total"]]     # ✅ keep Total so sort works
        .sum()
        .sort_values(by="Total", ascending=False)           # ✅ now valid
        .reset_index().head(10)
    )
    if(sport == "Overall"):
        return result
    else:
        return result[result["Sport"] == sport]

# heatmap of countries
def country_wise_data(final_df,country):
    result = (
    final_df
    .drop_duplicates(subset=["region", "Event", "Games", "Medal", "City", "Year", "NOC"])
    .dropna(subset=["Medal"])                                    # ✅ list, not string
    .pipe(lambda df: df[
        (df["region"] == country)        # ✅ & with parentheses, scoped to chain
    ]))

    return result.pivot_table(index="Sport",columns="Year",values="Medal",aggfunc="count").fillna(0)