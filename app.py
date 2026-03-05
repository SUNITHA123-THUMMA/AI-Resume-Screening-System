import streamlit as st
from utils import extract_text_from_pdf, clean_text
from model import calculate_similarity

st.title("AI Resume Screening System")

st.write("Upload Resume and Compare with Job Description")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

job_description = st.text_area("Paste Job Description Here")

if uploaded_file and job_description:
    
    resume_text = extract_text_from_pdf(uploaded_file)
    
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)
    
    score = calculate_similarity(cleaned_resume, cleaned_jd)
    
    st.subheader("Match Score")
    st.write(f"Resume matches {score}% with Job Description")
    
    if score > 75:
        st.success("High Match - Strong Candidate")
    elif score > 50:
        st.warning("Moderate Match")
    else:
        st.error("Low Match")