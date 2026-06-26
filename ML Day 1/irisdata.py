import pandas as pd
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()

# Convert to a DataFrame for cleaner exploration
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# Add the target (species) column
df['species'] = iris.target

# Map target integers to actual species names for readability
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species_name'] = df['species'].map(species_map)

# --- 3a. Dataset Shape ---
print("--- Dataset Shape ---")
print(df.shape) 
# Output: (150, 6) -> 150 rows, 6 columns

# --- 3b. Dataset Description ---
print("\n--- Statistical Description ---")
print(df.describe())

# --- 3c. Value Counts (Class Distribution) ---
print("\n--- Species Value Counts ---")
print(df['species_name'].value_counts())
