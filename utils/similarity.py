from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_description):

    # Store texts in list
    texts = [resume_text, job_description]

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Convert text into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Calculate cosine similarity
    similarity_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    # Convert score to percentage
    percentage = similarity_score[0][0] * 100

    return round(percentage, 2)