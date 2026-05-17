AI Resume Screening System

An AI-powered Resume Screening System built using Python, NLP, Machine Learning, and Streamlit.

This project compares resumes with job descriptions, calculates ATS-style match percentages, extracts matching skills, and ranks resumes automatically.

Features
Upload PDF resumes  
Extract text from resumes  
NLP-based preprocessing  
ATS-style skill matching  
Resume ranking system  
Match percentage calculation  
Dashboard analytics  
Data visualization charts  
Streamlit frontend UI  

Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- NLTK
- Scikit-learn
- PyPDF2

---
Project Structure

AI-Resume-Screening-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│ └── resumes/
│
├── utils/
│ ├── pdf_extractor.py
│ ├── preprocess.py
│ ├── similarity.py
│ └── skill_match.py
│
└── venv/

---

Installation

Step 1 — Clone Repository

```bash
git clone <repository-link>
```

Step 2 — Open Project Folder

```bash
cd AI-Resume-Screening-System
```

Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

Step 4 — Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Step 5 — Install Requirements

```bash
pip install -r requirements.txt
```

---

Run Project

```bash
streamlit run app.py
```

---
How It Works

1. Upload resume PDFs
2. Enter job description
3. Extract resume text
4. Perform NLP preprocessing
5. Extract matching skills
6. Calculate ATS match percentage
7. Rank resumes automatically
8. Display dashboard analytics

---

Machine Learning Concepts Used

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Skill Matching
- Resume Ranking Algorithm

---

Future Enhancements

- AI-based semantic matching
- Deep Learning resume analysis
- Resume feedback suggestions
- Online deployment
- Database integration
- User authentication

---
Author
Developed by [ Gilledi Santhosh]
