from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

# Load the spaCy English model once at the top
# We load it here so it doesn't reload every time the function is called
# Loading a model is slow - doing it once is efficient
nlp = spacy.load("en_core_web_lg")


def match_score(resume_text, jd_text):
    # Same as before - TF-IDF converts text to numbers, cosine similarity compares them
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return round(float(score[0][0]) * 100, 2)


def get_missing_skills(resume_text, jd_text):
    # Pass the JD text through spaCy - it analyzes every word
    # This is called "processing" the document
    jd_doc = nlp(jd_text)

    # Pass the resume text through spaCy as well
    resume_doc = nlp(resume_text)

    # Extract meaningful words from JD
    # We keep only NOUNS and PROPER NOUNS - these are where skills live
    # .text gets the actual word, .lower() makes it lowercase
    # token.is_alpha means we skip numbers and symbols
    # len(token) > 2 skips tiny words like "it", "be"
    jd_skills = set(
        token.lemma_.lower()
        for token in jd_doc
        if token.pos_ in ["NOUN", "PROPN"]
        and token.is_alpha
        and len(token) > 2
        and not token.is_stop
    )

    # Do the same for resume
    resume_skills = set(
        token.lemma_.lower()
        for token in resume_doc
        if token.pos_ in ["NOUN", "PROPN"]
        and token.is_alpha
        and len(token) > 2
        and not token.is_stop
    )

    # Find skills present in JD but missing from resume
    missing = jd_skills - resume_skills

    return sorted(list(missing))