#Data Cleaning

import pandas as pd
import numpy as np

# Load the CSV downloaded from API
df = pd.read_csv("mars_rover_photos_summary.csv")

# 1. Check data structure and missing values
print(df.info())
print(df.head())
print(df.isnull().sum())  # Which columns have missing values?

# 2. Fill or handle missing values
# The "camera" column has None (null) values, so we can fill them with the string "Unknown" for easier analysis later.
df['camera'] = df['camera'].fillna('Unknown')

# 3. Format adjustment
# Ensure the date is in datetime format for easier time-based analysis.
df['earth_date'] = pd.to_datetime(df['earth_date'])

# 4. Filter or transform columns
# For example, only look at data where photos were taken (total_photos > 0).
df_nonzero = df[df['total_photos'] > 0].copy()

# 5. Add calculated columns (Optional)
# Calculate the photo ratio (photo_count / total_photos) for all cameras on the same day for the same rover.
df_nonzero['photo_ratio'] = df_nonzero['photo_count'] / df_nonzero['total_photos']

# 6. Confirm data status after cleaning
print(df_nonzero.head())

# 7. Export the cleaned data for use in presentations or dashboards.
df_nonzero.to_csv("mars_rover_photos_summary_cleaned.csv", index=False)
print("Cleaned data saved to mars_rover_photos_summary_cleaned.csv")