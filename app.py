import streamlit as st
import pandas as pd

from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_match import (
    extract_skills,
    calculate_skill_match
)


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📌 Navigation")

st.sidebar.info(
    """
    AI Resume Screening System

    Upload resumes and compare them with job descriptions using NLP and Machine Learning.
    """
)

st.sidebar.success("✅ NLP Powered")
st.sidebar.success("✅ ATS-style Skill Matching")
st.sidebar.success("✅ Resume Ranking")
st.sidebar.success("✅ Dashboard Analytics")


# ---------------- MAIN TITLE ---------------- #

st.title("📄 AI Resume Screening System")

st.markdown(
    "### Smart Resume Screening using NLP & Machine Learning"
)


# ---------------- JOB DESCRIPTION ---------------- #

job_description = st.text_area(
    "Paste Job Description Here"
)


# ---------------- FILE UPLOAD ---------------- #

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)


# ---------------- PROCESS RESUMES ---------------- #

if uploaded_files and job_description:

    results = []

    # Extract job description skills
    jd_skills = extract_skills(job_description)

    for uploaded_file in uploaded_files:

        # Extract resume text
        resume_text = extract_text_from_pdf(uploaded_file)

        if not resume_text:

            st.error(
                f"Could not extract text from {uploaded_file.name}"
            )

            continue

        # Extract skills from resume
        resume_skills = extract_skills(resume_text)

        # Calculate ATS score
        score, matching_skills = calculate_skill_match(
            resume_skills,
            jd_skills
        )

        # Store results
        results.append({
            "Resume Name": uploaded_file.name,
            "ATS Score": score,
            "Matching Skills": ", ".join(matching_skills)
        })

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Sort by ATS score
    df = df.sort_values(
        by="ATS Score",
        ascending=False
    )

    # ---------------- DASHBOARD METRICS ---------------- #

    st.subheader("📊 Dashboard Analytics")

    total_resumes = len(df)

    highest_score = df["ATS Score"].max()

    top_candidate = df.iloc[0]["Resume Name"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Resumes",
            total_resumes
        )

    with col2:
        st.metric(
            "Highest ATS Score",
            f"{highest_score}%"
        )

    with col3:
        st.metric(
            "Top Candidate",
            top_candidate
        )

    st.divider()

    # ---------------- RESULTS TABLE ---------------- #

    st.subheader("📋 Resume Ranking Table")

    st.dataframe(df)

    st.divider()

    # ---------------- BAR CHART ---------------- #

    st.subheader("📈 ATS Score Visualization")

    chart_data = df.set_index("Resume Name")

    st.bar_chart(chart_data["ATS Score"])

    st.divider()

    # ---------------- DETAILED RESULTS ---------------- #

    st.subheader("🏆 Detailed Resume Analysis")

    for index, row in df.iterrows():

        st.info(f"📄 Resume: {row['Resume Name']}")

        st.metric(
            label="ATS Match Percentage",
            value=f"{row['ATS Score']}%"
        )

        st.progress(int(row["ATS Score"]))

        st.write("🛠 Matching Skills")

        if row["Matching Skills"]:

            st.success(row["Matching Skills"])

        else:
            st.warning("No matching skills found")

        st.divider()