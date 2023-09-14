# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_dataset.csv' with the actual dataset file)
# Assuming the dataset is in CSV format
df = pd.read_csv('your_dataset.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Summary statistics of numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Correlation matrix
correlation_matrix = df.corr()

# Plot a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Price Distribution
plt.figure(figsize=(8, 6))
sns.histplot(df['Price'], kde=True)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Property Size vs. Price
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Sqft', y='Price')
plt.title("Property Size vs. Price")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.show()

# Number of Bedrooms vs. Price
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Bedroom', y='Price')
plt.title("Number of Bedrooms vs. Price")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price")
plt.show()

# Floor vs. Price
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Floor', y='Price')
plt.title("Floor vs. Price")
plt.xlabel("Floor")
plt.ylabel("Price")
plt.xticks(rotation=90)
plt.show()
