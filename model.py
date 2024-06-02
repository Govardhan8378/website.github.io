import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data from the first CSV file
df1 = pd.read_csv('closings.csv')  # Replace 'closings.csv' with the path to your first CSV file

# Load data from the second CSV file
df2 = pd.read_csv('email_data.csv')  # Replace 'email_data.csv' with the path to your second CSV file

# Combine the textual data from both dataframes
corpus = list(df1['Closing']) + list(df2['Body'])

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
corpus = [doc for doc in corpus if not isinstance(doc, float) and not pd.isna(doc)]
# Fit and transform the textual data
tfidf_matrix = vectorizer.fit_transform(corpus)

# Calculate cosine similarity between the two sets of data
similarity_matrix = cosine_similarity(tfidf_matrix[:len(df1)], tfidf_matrix[len(df2):])

# Convert similarity scores to percentage scale
similarity_scores_percentage = similarity_matrix * 100

# Calculate the average similarity score
average_similarity_score = similarity_scores_percentage.mean()

print(f"Average similarity score: {average_similarity_score:.2f}%")
