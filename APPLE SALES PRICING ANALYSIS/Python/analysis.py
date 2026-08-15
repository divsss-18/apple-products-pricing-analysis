import pandas as pd
import numpy as np
df = pd.read_csv("../Dataset/apple_products_pricing_2020_2026.csv")

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nRandom 5 Records:")
print(df.sample(5))

print("\nStatistical Summary:")
print(df.describe())
print("\nPlatform-wise Product Count:")
print(df["Platform"].value_counts())


amazon = df[df["Platform"] == "Amazon"]

print("\nAmazon Products:")
print(amazon)


flipkart = df[df["Platform"] == "Flipkart"]
print("\nFlipkart Products:")
print(flipkart)
expensive = df[df["Launch_Price_USD"] > 1000]
print("\nProducts with Launch Price Above $1000:")
print(expensive)
cheap = df[df["Launch_Price_USD"] < 500]
print("\nProducts with Launch Price Below $500:")
print(cheap)
amazon_high_rating = df[
    (df["Platform"] == "Amazon") &
    (df["Rating"] > 4.5)
]

print("\nAmazon Products with Rating Above 4.5:")
print(amazon_high_rating)


result = df[
    (df["Platform"] == "Amazon") |
    (df["Rating"] > 4.8)
]

print("\nAmazon Products OR Products with Rating Above 4.8:")
print(result)


result = df[
    (df["Platform"] == "Amazon") &
    (df["Rating"] > 4.5) &
    (df["Reviews_Count"] > 100)
]

print("\nAmazon Products with Rating > 4.5 and Reviews > 100:")
print(result)


print("\nProducts Sorted by Rating:")
print(df.sort_values(by="Rating", ascending=False))


print("\nProducts Sorted by Current Price:")
print(df.sort_values(by="Current_Price_INR"))


print("\nProducts Sorted by Reviews:")
print(df.sort_values(by="Reviews_Count", ascending=False))


print("\nProducts Sorted by Platform and Rating:")
print(
    df.sort_values(
        by=["Platform", "Rating"],
        ascending=[True, False]
    )
)


print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Records:")
print(df.duplicated().sum())
print("\nAverage Price by Platform:")
print(
    df.groupby("Platform")["Current_Price_INR"].mean()
)
print("\nAverage Rating by Platform:")
print(
    df.groupby("Platform")["Rating"].mean()
)


print("\nNumber of Products by Platform:")
print(
    df.groupby("Platform").size()
)
df = df.drop_duplicates()
print("\nDataset Shape After Removing Duplicates:")
print(df.shape)
df.to_csv(
    "Dataset/cleaned_apple_products.csv",
    index=False
)
print("\nCleaned dataset saved successfully!")