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

## Live Demo

[Click here to try the live app]([YOUR_STREAMLIT_URL_HERE](https://resume-matcher-mmetptxcw5t3t9nnkkfsnw.streamlit.app/))
