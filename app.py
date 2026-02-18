import streamlit as st

st.set_page_config(page_title="Resume Matcher")

st.title("Resume to Job Description Matcher")

st.write("Upload your resume and paste a Job Description to see how well you match.")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste the Job Description here", height=250)

if st.button("Check Match Score"):
    st.write("Button clicked! Logic coming soon.")