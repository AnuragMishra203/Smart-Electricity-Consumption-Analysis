import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(
    "E:\DATA ANALYSIS\smart_electric_consumption_analysis\data\household_power_consumption.txt",
    sep=";",
    low_memory=False
)

df.replace("?", np.nan, inplace=True)

#Checking for '?' values:

for col in df.columns:
    count = (df[col] == "?").sum()
    if count > 0:
        print(f"{col}: {count}")

#cehcking for null values
#print(df.isnull().sum())
 
numeric_columns = ["Global_active_power", "Global_reactive_power", "Voltage", "Global_intensity", "Sub_metering_1", "Sub_metering_2", "Sub_metering_3"]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col])

# Combine Date and Time into one DateTime column
df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], dayfirst=True)

#set datetime as index and remove the original Date and Time columns

df.set_index("datetime",inplace=True)
df.drop(columns=["Date", "Time"], inplace=True)

#find percentage of null values in each column

#print(df.isnull().sum())
total_missing_values = df.isnull().sum().sum()
#print("Total missing values:", total_missing_values)
missing_percentage = (df.isnull().sum()/len(df))*100
#print(missing_percentage)
 
 # since the missing values are less than 5% of the total data, we can drop them
df=df.dropna()

#check duplicate rows in the dataset and remove them
#duplicates = df.duplicated().sum()
df = df.drop_duplicates()
duplicates = df.duplicated().sum()
print("Number of duplicate rows:", duplicates)

#save the cleaned dataset to a new CSV file
df.to_csv("cleaned_household_power_consumption.csv")