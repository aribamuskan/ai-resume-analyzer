# 🤖 AI Resume Analyzer

<p align="center">
  <strong>AI-powered resume analysis and job matching application built with Python, NLP, Scikit-learn, and Streamlit.</strong>
</p>

<p align="center">
  <a href="https://ai-resume-analyzer-tgizmr6jxeoysucypnyjdp.streamlit.app/">
    🚀 <strong>Live Demo</strong>
  </a>
  &nbsp; | &nbsp;
  <a href="https://github.com/aribamuskan/ai-resume-analyzer">
    💻 <strong>GitHub Repository</strong>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-8A2BE2?style=for-the-badge">
  <img src="https://img.shields.io/badge/PDF-pypdf-red?style=for-the-badge">
</p>

---

## 🚀 Live Demo

### Try the application online

**Live Application:**  
https://ai-resume-analyzer-tgizmr6jxeoysucypnyjdp.streamlit.app/

The application is deployed using **Streamlit Community Cloud** and can be accessed directly from a web browser.

---

## 📌 Overview

**AI Resume Analyzer** is an AI-powered web application that analyzes a candidate's resume against a specific job description.

The application accepts a **PDF resume** and a **job description**, extracts and processes their content, identifies relevant technical skills and keywords, calculates text similarity, evaluates skill matching, checks resume completeness, and generates actionable recommendations.

The project demonstrates a practical implementation of:

- Natural Language Processing
- Text preprocessing
- TF-IDF
- Cosine Similarity
- Skill extraction
- Keyword analysis
- Rule-based resume analysis
- PDF text extraction
- Interactive Streamlit applications

---

## 🎯 Problem Statement

Job seekers often need to customize their resumes for different job opportunities.

Manually comparing a resume with every job description can be time-consuming. Candidates may also miss important technical skills, keywords, or resume sections required for a particular role.

This project provides an automated way to analyze a resume and identify how closely it matches a given job description.

---

## 💡 Solution

The AI Resume Analyzer processes both the resume and job description and generates a structured analysis.

The application provides:

- Overall Resume Match Score
- Text Similarity Score
- Skill Match Score
- Matching Skills
- Missing Skills
- Resume Skills
- Resume Completeness
- ATS Keyword Analysis
- Resume Improvement Suggestions
- Skill Development Recommendations

---

# ✨ Key Features

## 📄 Resume PDF Analysis

- Upload a resume in PDF format.
- Extract resume text automatically.
- Process the extracted content.
- Detect technical skills from the resume.

## 🎯 Job Description Matching

Compare the resume with a target job description and calculate:

- Overall Match Score
- Text Similarity Score
- Skill Match Score

## 🧠 Skill Analysis

The application identifies technical skills from both the resume and job description.

It displays:

- ✅ Matching Skills
- ❌ Missing Skills
- 📊 Skill Match Percentage
- 📚 Recommendations for missing skills

## 💼 Resume Health Analysis

The application checks important resume sections including:

- Contact Information
- Professional Summary
- Skills
- Experience
- Projects
- Education

A **Resume Completeness Score** is calculated based on the detected sections.

## 🔎 ATS Keyword Analysis

The application analyzes important keywords from the job description and checks whether those keywords are present in the resume.

This helps candidates identify potentially important keywords that may need to be added or emphasized.

## 💡 Resume Improvement Suggestions

The application generates suggestions based on:

- Missing resume sections
- Missing skills
- Job requirements
- Detected resume gaps

## 📚 Skill Development Recommendations

If the job description contains skills that are not detected in the resume, the application provides learning recommendations for those skills.

## 🎨 Professional User Interface

The application includes:

- Modern responsive design
- Professional dashboard layout
- Resume upload interface
- Job description input
- Score cards
- Skill badges
- Resume health indicators
- ATS analysis
- Recommendation cards
- Responsive layout

---

# 📊 Analysis Results

| Metric | Description |
|---|---|
| **Overall Match Score** | Combined indication of resume-job matching |
| **Text Similarity Score** | Similarity between resume and job description |
| **Skill Match Score** | Percentage of required skills detected in the resume |
| **Resume Completeness** | Percentage of important resume sections detected |
| **Matching Skills** | Skills found in both resume and job description |
| **Missing Skills** | Required skills not detected in the resume |
| **ATS Keywords** | Important job-description keywords checked against the resume |

---

# 🧠 NLP & Machine Learning Approach

## 1. PDF Text Extraction

The uploaded resume is processed using **pypdf** to extract text from the PDF document.

The workflow begins with:

**Resume PDF → Text Extraction → Resume Text**

## 2. Text Preprocessing

The extracted resume and job description text are normalized before analysis.

The preprocessing includes:

- Converting text to lowercase
- Removing unnecessary whitespace
- Preparing text for vectorization
- Normalizing content for comparison

## 3. TF-IDF Vectorization

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert the resume and job description into numerical vectors.

TF-IDF helps represent the importance of terms within the documents.

**Resume Text + Job Description → TF-IDF Vectorization → Numerical Vectors**

## 4. Cosine Similarity

After converting the documents into TF-IDF vectors, **Cosine Similarity** is used to measure the similarity between the resume and job description.

The similarity value is converted into a percentage for easier interpretation.

**TF-IDF Resume Vector + TF-IDF Job Vector → Cosine Similarity → Text Similarity Score**

## 5. Skill Matching

A predefined technical skill vocabulary is used to identify skills in the resume and job description.

The application then determines:

- Required job skills
- Skills detected in the resume
- Matching skills
- Missing skills
- Skill match percentage

---

# 🧩 Skills Analyzed

The application can identify a range of technical skills.

### Programming & Development

- Python
- HTML
- CSS
- JavaScript
- React
- SQL

### Machine Learning & Artificial Intelligence

- Machine Learning
- Artificial Intelligence
- Deep Learning
- NLP
- Scikit-learn
- TensorFlow
- Keras
- PyTorch

### Data & Analytics

- Pandas
- NumPy
- Power BI
- Excel

### Tools & Deployment

- Streamlit
- Git
- GitHub
- Docker
- AWS

---

# 🔄 Application Workflow

**Upload Resume PDF**  
↓  
**Extract Resume Text**  
↓  
**Enter Job Description**  
↓  
**Text Preprocessing**  
↓  
**TF-IDF & Cosine Similarity**  
↓  
**Skill Extraction & Matching**  
↓  
**Resume Health Analysis**  
↓  
**ATS Keyword Analysis**  
↓  
**Generate Recommendations**  
↓  
**Display Final Analysis Dashboard**

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application and user interface |
| **Scikit-learn** | TF-IDF and cosine similarity |
| **pypdf** | PDF text extraction |
| **Regex** | Contact and section detection |
| **HTML/CSS** | Custom professional interface |
| **Git** | Version control |
| **GitHub** | Source code hosting |
| **Streamlit Community Cloud** | Application deployment |

---

# 📂 Project Structure

    AI_Resume_Analyzer/
    │
    ├── app.py
    ├── resume_analyzer.py
    ├── requirements.txt
    ├── sample_resume.pdf
    ├── README.md
    └── .git/

### File Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application and user interface |
| `resume_analyzer.py` | Resume analysis functionality |
| `requirements.txt` | Python dependencies |
| `sample_resume.pdf` | Sample resume used for testing |
| `README.md` | Project documentation |
| `.git/` | Local Git repository metadata |

---

# ⚙️ Installation

## 1. Clone the Repository

    git clone https://github.com/aribamuskan/ai-resume-analyzer.git

## 2. Navigate to the Project Directory

    cd ai-resume-analyzer

## 3. Install Dependencies

    pip install -r requirements.txt

---

# ▶️ Run Locally

Start the application using:

    python -m streamlit run app.py

The application will open in your default web browser.

---

# 🧪 How to Use

### Step 1 — Upload Resume

Upload your resume as a PDF file.

### Step 2 — Enter Job Description

Paste the complete job description into the provided text area.

### Step 3 — Analyze Resume

Click the **Analyze Resume** button.

### Step 4 — Review Results

The application generates:

- Overall Match Score
- Text Similarity
- Skill Match
- Matching Skills
- Missing Skills
- Resume Skills
- Resume Health
- ATS Keywords
- Resume Improvement Suggestions
- Skill Development Recommendations

---

# 🎯 Example Use Case

Suppose a company is hiring for a **Machine Learning Engineer** and the job description requires:

- Python
- Machine Learning
- NLP
- TensorFlow
- SQL
- Git
- Docker
- AWS

The application can compare these requirements against the uploaded resume and identify which skills are detected and which are missing.

For example:

### Matching Skills

- Python
- Machine Learning
- NLP
- Git

### Missing Skills

- TensorFlow
- SQL
- Docker
- AWS

The application can then provide recommendations for improving the candidate's skills and resume.

---

# 📈 Project Highlights

This project demonstrates practical experience with:

- Python programming
- Natural Language Processing
- Text similarity
- TF-IDF
- Cosine similarity
- Skill extraction
- Keyword analysis
- PDF processing
- Regex-based text analysis
- Streamlit application development
- Custom UI design
- Git and GitHub
- Cloud deployment

---

# 🔐 Privacy Note

The application analyzes the resume content provided by the user for generating analysis results.

Users should avoid uploading confidential or sensitive documents unless they are comfortable with the hosting environment and its data-handling policies.

---

# ⚠️ Limitations

The current version uses:

- A predefined technical skill vocabulary
- Rule-based skill detection
- TF-IDF-based text similarity
- Keyword-based ATS analysis
- Pattern-based resume section detection

Therefore, the generated results should be considered **automated guidance rather than a definitive evaluation of a candidate or resume**.

---

# 🚀 Future Improvements

Future versions could include:

- 🤖 Transformer-based NLP models
- 🧠 Semantic embeddings for improved job matching
- 📑 DOCX resume support
- 📊 Advanced ATS scoring
- ✍️ AI-generated resume improvement suggestions
- 🎯 Job-role-specific skill analysis
- 🔄 Resume comparison across multiple job descriptions
- 📄 Automated resume report generation
- 📈 Resume version comparison
- 🔐 User accounts and resume history
- 🌐 Multi-language resume analysis

---

# 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### 🚀 Live Application

https://ai-resume-analyzer-tgizmr6jxeoysucypnyjdp.streamlit.app/

### 💻 GitHub Repository

https://github.com/aribamuskan/ai-resume-analyzer

---

# 👩‍💻 Author

## Ariba Muskan

**Software Engineering Student | AI & Machine Learning Learner**

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Python
- AI-powered Applications
- Software Development

---

# 🔗 Project Links

| Resource | Link |
|---|---|
| 🚀 **Live Demo** | https://ai-resume-analyzer-tgizmr6jxeoysucypnyjdp.streamlit.app/ |
| 💻 **GitHub Repository** | https://github.com/aribamuskan/ai-resume-analyzer |

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

<p align="center">
  Built with ❤️ using Python, NLP, Scikit-learn & Streamlit
</p>