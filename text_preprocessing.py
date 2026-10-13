import pandas as pd
import re
import nltk

# Download required NLTK data (only first time)
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load cleaned dataset
df = pd.read_csv("data/reviews.csv")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to clean text
def preprocess(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Split into words
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

# Apply preprocessing
df["Cleaned_Review"] = df["Review"].apply(preprocess)

print(df)

# Save new dataset
df.to_csv("data/preprocessed_reviews.csv", index=False)

print("\n✅ Text preprocessing completed successfully!")