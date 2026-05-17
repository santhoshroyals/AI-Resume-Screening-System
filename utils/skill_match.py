def extract_skills(text):

    # Skill database
    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
        "pandas",
        "numpy",
        "data analysis",
        "data visualization",
        "excel",
        "power bi",
        "cloud computing",
        "java",
        "c++",
        "tableau"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    return found_skills


# Calculate skill matching percentage
def calculate_skill_match(resume_skills, jd_skills):

    matching_skills = []

    for skill in resume_skills:

        if skill in jd_skills:
            matching_skills.append(skill)

    # Avoid division by zero
    if len(jd_skills) == 0:
        return 0, []

    match_percentage = (
        len(matching_skills) / len(jd_skills)
    ) * 100

    return round(match_percentage, 2), matching_skills