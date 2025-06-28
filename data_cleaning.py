import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('custSup.csv')

# Step A: Drop rows with missing target (Customer Satisfaction Rating)
df = df.dropna(subset=['Customer Satisfaction Rating'])

# Step B: Convert date/time columns to datetime
df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'], errors='coerce')
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce')
df['Time to Resolution'] = pd.to_datetime(df['Time to Resolution'], errors='coerce')

# Step C: Handle missing values
# Fill missing 'Resolution' with 'No resolution'
df['Resolution'] = df['Resolution'].fillna('No resolution')

# For 'Time to Resolution', fill missing with median time difference (in days)
median_time_diff = (df['Time to Resolution'] - df['First Response Time']).median()
df['Time to Resolution'] = df['Time to Resolution'].fillna(df['First Response Time'] + median_time_diff)

# Step D: Check categorical columns and clean if needed
categorical_cols = ['Customer Gender', 'Product Purchased', 'Ticket Type', 'Ticket Status', 'Ticket Priority', 'Ticket Channel']

for col in categorical_cols:
    df[col] = df[col].str.strip().str.lower()

# Step E: Feature engineering from dates
df['Response Delay Minutes'] = (df['First Response Time'] - df['Date of Purchase']).dt.total_seconds() / 60
df['Resolution Time Hours'] = (df['Time to Resolution'] - df['First Response Time']).dt.total_seconds() / 3600
df['Purchase DayOfWeek'] = df['Date of Purchase'].dt.day_name()

# *** New Step: Remove rows where resolution time is negative ***
df = df[df['Resolution Time Hours'] >= 0]

# Drop or keep columns as needed — Ticket ID likely not useful as feature
df = df.drop(columns=['Ticket ID'])

# Final check for any remaining missing values
print("Missing values after cleaning:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv('custSup_cleaned.csv', index=False)
