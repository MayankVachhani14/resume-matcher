from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_score(resume_text, jd_text):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])

    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return round(float(score[0][0]) * 100, 2)