import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
# Make sure to update the file path to where you've saved the Titanic dataset
data = pd.read_csv('train.csv')

# Check the first few rows of the dataset to understand its structure
print(data.head())

# Histogram for age distribution
plt.figure(figsize=(10, 5))
plt.hist(data['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')  # Drop missing values
plt.title('Age Distribution in Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
