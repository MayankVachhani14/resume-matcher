import streamlit as st

from utils import extract_text_from_pdf
from matcher import match_score

st.set_page_config(page_title="Resume Matcher")

st.title("Resume to Job Description Matcher")

st.write("Upload your resume and paste a Job Description to see how well you match.")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste the Job Description here", height=250)

if st.button("Check Match Score"):
        
        if uploaded_resume is None or job_description.strip() == "":
            st.warning("Please upload a resume and paste a job description.")

        else:
            resume_text = extract_text_from_pdf(uploaded_resume)

            score = match_score(resume_text, job_description)

            st.divider()

            st.metric(label="Match Score", value=f"{score} / 100")

            if score >= 70:
                st.success("Strong Match! Your resume aligns well with this job.")
            elif score >= 40:
                st.warning("Moderate Match. Consider adding more relevant keywords.")
            else:
                st.error("Low Match. Your resume needs more alignment with this JD.")