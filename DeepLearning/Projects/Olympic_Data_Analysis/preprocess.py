import pandas as pd

def preprocess_data(df, region_df):

    # Filter Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Merge regions
    df = df.merge(region_df, on="NOC", how="left")

    # Remove duplicate medals in team events
    df.drop_duplicates(
        subset=['Team','NOC','Games','Year','Sport','Event','Medal'],
        inplace=True
    )

    # Create medal dummy columns
    df = pd.concat(
        [df, pd.get_dummies(df['Medal']).astype(int)],
        axis=1
    )

    return df