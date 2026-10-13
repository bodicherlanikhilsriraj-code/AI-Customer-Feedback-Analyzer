import pandas as pd

# Read the CSV file
df = pd.read_csv("data/reviews.csv")

# Display the first 5 rows
print(df.head())

# Show dataset information
print("\nDataset Information:")
print(df.info())
