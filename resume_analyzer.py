from pypdf import PdfReader
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def extract_skills(text):
    skills = [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "NLP",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "Keras",
        "PyTorch",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Streamlit",
        "Git",
        "GitHub",
        "Docker",
        "AWS",
        "Power BI",
        "Excel"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills


def calculate_similarity(resume_text, job_description):
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return score


def calculate_skill_match(resume_skills, job_skills):
    if len(job_skills) == 0:
        return 0

    matched_count = len(
        set(resume_skills) & set(job_skills)
    )

    score = (matched_count / len(job_skills)) * 100

    return score


def generate_recommendations(missing_skills):
    recommendations = {
        "Python": "Improve Python programming and problem-solving skills.",
        "Machine Learning": "Practice machine learning algorithms and real-world projects.",
        "Deep Learning": "Learn neural networks and deep learning frameworks.",
        "Artificial Intelligence": "Study core AI concepts and practical AI applications.",
        "NLP": "Learn text preprocessing, TF-IDF, embeddings, and NLP models.",
        "Pandas": "Practice data manipulation and analysis using pandas.",
        "NumPy": "Practice numerical computing and array operations with NumPy.",
        "Scikit-learn": "Build more machine learning projects using scikit-learn.",
        "TensorFlow": "Learn TensorFlow for deep learning and neural network development.",
        "Keras": "Practice building neural networks using Keras.",
        "PyTorch": "Learn PyTorch for deep learning and model development.",
        "SQL": "Practice SQL queries, joins, filtering, grouping, and databases.",
        "HTML": "Improve HTML fundamentals and semantic webpage structure.",
        "CSS": "Practice responsive layouts, Flexbox, and CSS Grid.",
        "JavaScript": "Strengthen JavaScript fundamentals and DOM manipulation.",
        "React": "Learn React components, state, props, and API integration.",
        "Streamlit": "Build interactive machine learning applications with Streamlit.",
        "Git": "Practice Git version control, branching, and collaboration workflows.",
        "GitHub": "Practice GitHub repositories, pull requests, and project collaboration.",
        "Docker": "Learn Docker containers and how to containerize applications.",
        "AWS": "Learn AWS cloud fundamentals and basic cloud deployment.",
        "Power BI": "Practice dashboards, data visualization, and business analytics.",
        "Excel": "Improve Excel formulas, data analysis, and reporting."
    }

    suggestions = []

    for skill in missing_skills:
        if skill in recommendations:
            suggestions.append(recommendations[skill])

    return suggestions


# --------------------------------
# 1. Read Resume
# --------------------------------

pdf_path = "sample_resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)

cleaned_resume = clean_text(resume_text)


# --------------------------------
# 2. Extract Resume Skills
# --------------------------------

resume_skills = extract_skills(cleaned_resume)


# --------------------------------
# 3. Job Description
# --------------------------------

job_description = """
We are looking for a Machine Learning Engineer
with experience in Python, Machine Learning,
SQL, TensorFlow, AWS and Docker.

The candidate should also understand
data analysis, NLP and Git.
"""

cleaned_job_description = clean_text(job_description)


# --------------------------------
# 4. Extract Job Skills
# --------------------------------

job_skills = extract_skills(cleaned_job_description)


# --------------------------------
# 5. Matched Skills
# --------------------------------

matched_skills = []

for skill in resume_skills:
    if skill in job_skills:
        matched_skills.append(skill)


# --------------------------------
# 6. Missing Skills
# --------------------------------

missing_skills = []

for skill in job_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)


# --------------------------------
# 7. Text Similarity
# --------------------------------

text_similarity_score = calculate_similarity(
    cleaned_resume,
    cleaned_job_description
)


# --------------------------------
# 8. Skill Match Score
# --------------------------------

skill_match_score = calculate_skill_match(
    resume_skills,
    job_skills
)


# --------------------------------
# 9. Overall Match Score
# --------------------------------

overall_match_score = (
    (text_similarity_score * 0.40)
    +
    (skill_match_score * 0.60)
)


# --------------------------------
# 10. Recommendations
# --------------------------------

recommendations = generate_recommendations(
    missing_skills
)


# --------------------------------
# 11. Display Results
# --------------------------------

print("\nRESUME SKILLS")
print("----------------")

for skill in resume_skills:
    print("✓", skill)


print("\nJOB REQUIRED SKILLS")
print("----------------")

for skill in job_skills:
    print("✓", skill)


print("\nMATCHED SKILLS")
print("----------------")

for skill in matched_skills:
    print("✓", skill)


print("\nMISSING SKILLS")
print("----------------")

for skill in missing_skills:
    print("✗", skill)


print("\nTEXT SIMILARITY SCORE")
print("----------------")

print(f"{text_similarity_score:.2f}%")


print("\nSKILL MATCH SCORE")
print("----------------")

print(f"{skill_match_score:.2f}%")


print("\nOVERALL MATCH SCORE")
print("----------------")

print(f"{overall_match_score:.2f}%")


print("\nRECOMMENDATIONS")
print("----------------")

for recommendation in recommendations:
    print("→", recommendation)