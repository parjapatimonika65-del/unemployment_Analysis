# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("unemployment in india.csv")

# First 5 rows
print(df.head())

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Rename columns (if needed)
df.columns = df.columns.str.strip()

# Show columns
print(df.columns)

# Basic statistics
print(df.describe())

# Visualization

plt.figure(figsize=(10,5))

# Replace column name according to dataset
sns.lineplot(
x=df["Date"],
y=df["Estimated Unemployment Rate (%)"]
)

plt.title("Unemployment Rate Trend")
plt.xticks(rotation=45)

plt.show()