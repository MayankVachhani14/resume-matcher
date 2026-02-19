# Resume to Job Description Matcher

A machine learning web application that scores how well a resume matches a job description.

## Problem

Recruiters spend significant time manually screening resumes before identifying suitable candidates. This tool automates the initial screening by providing a match score and highlighting skill gaps instantly.

## What It Does

- Upload multiple resumes in PDF format
- Paste any job description
- Get a match score out of 100 for each resume
- See which skills are missing from each resume based on the job description
- Resumes are ranked from highest to lowest match automatically

## How It Works

The scoring uses TF-IDF vectorization combined with cosine similarity to mathematically compare the resume and job description text. Skill extraction is powered by KeyBERT, a BERT-based NLP model that identifies the most contextually important keywords from the job description and checks their presence in the resume.

## Tech Stack

- Python
- Streamlit
- scikit-learn
- KeyBERT
- pdfplumber

## Run Locally

Clone the repository and navigate into the folder:

git clone https://github.com/MayankVachhani14/resume-matcher.git
cd resume-matcher

Create and activate a virtual environment:

python3.11 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

## Live Demo

[Click here to try the live app](YOUR_STREAMLIT_URL_HERE)
