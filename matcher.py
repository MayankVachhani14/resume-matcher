from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from keybert import KeyBERT

# Load the KeyBERT model once at the top
# Same reason as before - loading is slow, so we do it once
kw_model = KeyBERT()


def match_score(resume_text, jd_text):
    # Same as always - TF-IDF + cosine similarity
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return round(float(score[0][0]) * 100, 2)


def get_missing_skills(resume_text, jd_text):
    # KeyBERT extracts the most important keywords from the JD
    # keyphrase_ngram_range=(1,2) means it can extract single words AND two word phrases
    # So it can find both "Python" and "machine learning" not just single words
    # top_n=20 means extract the top 20 most important keywords
    # stop_words="english" automatically removes common English words
    jd_keywords = kw_model.extract_keywords(
        jd_text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=20
    )

    # kw_model returns a list of tuples like [("python", 0.85), ("machine learning", 0.79)]
    # The first item is the keyword, second is the confidence score
    # We only keep keywords with confidence above 0.3 - anything lower is likely noise
    jd_skills = set(
        keyword for keyword, score in jd_keywords
        if score > 0.3
    )

    # Do the same for resume to find what skills the candidate already has
    resume_keywords = kw_model.extract_keywords(
        resume_text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=30
    )

    resume_skills = set(
        keyword for keyword, score in resume_keywords
        if score > 0.3
    )

    # Find skills in JD that are not in resume
    missing = jd_skills - resume_skills

    return sorted(list(missing))