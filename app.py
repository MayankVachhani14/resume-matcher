import streamlit as st
from utils import extract_text_from_pdf
from matcher import match_score, get_missing_skills

# Page config
st.set_page_config(page_title="Resume Matcher", layout="wide")

# Title
st.title("Resume to Job Description Matcher")
st.write("Upload multiple resumes and paste a Job Description to compare candidates.")

# Two columns side by side - left for resumes, right for JD
col1, col2 = st.columns(2)

with col1:
    # accept_multiple_files=True allows uploading more than one PDF
    uploaded_resumes = st.file_uploader(
        "Upload Resumes (PDF)", 
        type=["pdf"], 
        accept_multiple_files=True
    )

with col2:
    job_description = st.text_area("Paste the Job Description here", height=300)

# Button to trigger matching
if st.button("Match Resumes"):

    # Validate - make sure user uploaded at least one resume and pasted JD
    if not uploaded_resumes or job_description.strip() == "":
        st.warning("Please upload at least one resume and paste a job description.")

    else:
        st.divider()
        st.subheader("Results")

        # We create an empty list to store results for all resumes
        results = []

        # Loop through every uploaded resume one by one
        for resume_file in uploaded_resumes:

            # Extract text from this resume
            resume_text = extract_text_from_pdf(resume_file)

            # Calculate match score for this resume
            score = match_score(resume_text, job_description)

            # Get missing skills for this resume
            missing = get_missing_skills(resume_text, job_description)

            # Store everything in a dictionary and add to results list
            results.append({
                "name": resume_file.name,
                "score": score,
                "missing": missing
            })

        # Sort results by score - highest score appears first
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # Now display results for each resume
        for result in results:

            # Show resume name and score side by side
            st.markdown(f"### {result['name']}")
            st.metric(label="Match Score", value=f"{result['score']} / 100")

            # Show colored banner based on score
            if result["score"] >= 70:
                st.success("Strong Match!")
            elif result["score"] >= 40:
                st.warning("Moderate Match")
            else:
                st.error("Low Match")

            # Show missing skills in a clean expandable section
            # expander hides the details until user clicks it - keeps UI clean
            with st.expander("View Missing Skills"):
                if result["missing"]:
                    # We join all missing skills with a comma and show them
                    st.write(", ".join(result["missing"][:30]))
                    st.caption("Showing top 30 missing keywords from the Job Description")
                else:
                    st.write("No major missing skills found!")

            st.divider()