import pandas as pd

# Load dataset
df = pd.read_csv("data/reviews.csv")

print("Original Dataset")
print(df)

# Check for missing values
print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset after removing duplicates")
print(df)

# Save the cleaned dataset
df.to_csv("data/cleaned_reviews.csv", index=False)

print("\nCleaned dataset saved successfully!")