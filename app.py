import html
import re

import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# DESIGN SYSTEM
# =========================================================
st.markdown(
    """
    <style>
    :root {
        --ink: #14213d;
        --muted: #68758b;
        --blue: #4263eb;
        --purple: #7357e8;
        --line: #e7ebf3;
        --surface: #ffffff;
    }

    .stApp {
        background:
            radial-gradient(circle at 7% 2%, rgba(99, 102, 241, .07), transparent 24rem),
            #f5f7fc;
        color: var(--ink);
    }

    .block-container {
        max-width: 1220px;
        padding-top: 1.6rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer {visibility: hidden;}
    header[data-testid="stHeader"] {background: transparent;}

    /* Hero banner */
    .hero-wrap {
        position: relative;
        overflow: hidden;
        display: grid;
        grid-template-columns: 1.15fr .85fr;
        align-items: center;
        gap: 1.25rem;
        min-height: 350px;
        padding: 2.6rem 3rem;
        margin-bottom: 2.1rem;
        color: #fff;
        border-radius: 28px;
        background: linear-gradient(118deg, #111b3c 0%, #243b82 55%, #6047cf 100%);
        box-shadow: 0 22px 55px rgba(34, 48, 104, .19);
    }

    .hero-wrap:before {
        content: "";
        position: absolute;
        width: 360px;
        height: 360px;
        right: -130px;
        top: -190px;
        border-radius: 50%;
        background: rgba(255,255,255,.08);
    }

    .hero-copy, .hero-art {position: relative; z-index: 1;}
    .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 12px;
        margin-bottom: 18px;
        border: 1px solid rgba(255,255,255,.23);
        border-radius: 999px;
        background: rgba(255,255,255,.09);
        color: #e3eaff;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: .09em;
        text-transform: uppercase;
    }

    .hero-title {
        max-width: 620px;
        margin: 0 0 15px;
        color: #fff;
        font-size: clamp(2.15rem, 4vw, 3.5rem);
        line-height: 1.08;
        font-weight: 800;
        letter-spacing: -.045em;
    }

    .hero-title span {color: #aebdff;}
    .hero-subtitle {
        max-width: 590px;
        margin: 0 0 24px;
        color: #d8e1ff;
        font-size: 15px;
        line-height: 1.8;
    }

    .hero-pills {display:flex; flex-wrap:wrap; gap:8px;}
    .hero-pill {
        padding: 8px 11px;
        border-radius: 10px;
        color: #f3f5ff;
        background: rgba(255,255,255,.10);
        border: 1px solid rgba(255,255,255,.13);
        font-size: 12px;
        font-weight: 600;
    }

    .hero-art {display:flex; justify-content:center; align-items:center; min-width:0;}
    .hero-art svg {width:100%; max-width:410px; height:auto; filter: drop-shadow(0 18px 22px rgba(4, 10, 35, .20));}

    /* Section headings */
    .section-kicker {
        margin: 0 0 7px;
        color: #6475c7;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
    }
    .section-title {
        margin: 0 0 7px;
        color: var(--ink);
        font-size: 25px;
        font-weight: 800;
        letter-spacing: -.035em;
    }
    .section-description {
        margin: 0 0 22px;
        color: var(--muted);
        font-size: 14px;
        line-height: 1.65;
    }

    /* Input cards */
    .input-card {
        padding: 20px 22px 15px;
        border: 1px solid var(--line);
        border-radius: 18px 18px 0 0;
        background: #fff;
        box-shadow: 0 7px 25px rgba(25, 40, 80, .045);
    }
    .input-card-title {display:flex; align-items:center; gap:10px; margin-bottom:7px; color:var(--ink); font-size:16px; font-weight:750;}
    .icon-tile {
        display:inline-flex; align-items:center; justify-content:center;
        width:36px; height:36px; border-radius:11px;
        color:#4358d8; background:#eef1ff; font-size:17px;
    }
    .input-card-desc {padding-left:46px; color:var(--muted); font-size:13px; line-height:1.55;}

    /* Streamlit widgets */
    [data-testid="stFileUploaderDropzone"] {
        min-height: 170px;
        border: 1.5px dashed #c8d1e5 !important;
        border-radius: 0 0 18px 18px !important;
        background: #fff !important;
    }
    [data-testid="stFileUploaderDropzone"]:hover {border-color:#7888ed !important; background:#fbfcff !important;}
    [data-testid="stFileUploaderDropzone"] button {
        color: #3f56d8 !important;
        background: #eef1ff !important;
        border: 1px solid #dce2ff !important;
        border-radius: 9px !important;
        font-weight: 700 !important;
    }
    [data-testid="stFileUploaderDropzoneInstructions"] small {color:#7a859a !important;}
    .stTextArea textarea {
        min-height: 170px;
        border: 1px solid #e0e5ef !important;
        border-radius: 0 0 18px 18px !important;
        background: #fff !important;
        color: #17233f !important;
        font-size: 14px !important;
        line-height: 1.65 !important;
        padding: 15px !important;
    }
    .stTextArea textarea:focus {
        border-color: #8a97f2 !important;
        box-shadow: 0 0 0 3px rgba(91, 105, 232, .10) !important;
    }
    .stTextArea label, .stFileUploader label {display:none;}

    .stButton > button[kind="primary"] {
        width:100%; min-height:54px;
        border:0 !important; border-radius:14px !important;
        color:#fff !important;
        background:linear-gradient(100deg,#4263eb,#7357e8) !important;
        font-size:15px !important; font-weight:800 !important;
        box-shadow:0 10px 22px rgba(76, 88, 220, .20);
        transition:transform .18s ease, box-shadow .18s ease;
    }
    .stButton > button[kind="primary"]:hover {
        transform:translateY(-1px);
        box-shadow:0 13px 26px rgba(76, 88, 220, .27);
    }

    /* Results */
    .results-banner {
        display:flex; justify-content:space-between; align-items:center; gap:16px;
        padding:20px 24px; margin: 8px 0 18px;
        border:1px solid #e4e8f4; border-radius:18px; background:#fff;
        box-shadow:0 8px 25px rgba(25,40,80,.045);
    }
    .results-title {color:var(--ink); font-size:21px; font-weight:800; letter-spacing:-.03em;}
    .results-subtitle {margin-top:5px; color:var(--muted); font-size:13px;}
    .status-chip {white-space:nowrap; padding:8px 12px; border-radius:999px; background:#eef2ff; color:#4657c9; font-size:12px; font-weight:800;}

    .score-card {
        height:100%; min-height:155px; padding:21px;
        border:1px solid var(--line); border-radius:18px; background:#fff;
        box-shadow:0 8px 24px rgba(25,40,80,.045);
    }
    .score-top {display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:16px;}
    .score-label {color:#68758b; font-size:13px; font-weight:700;}
    .score-icon {display:flex; align-items:center; justify-content:center; width:34px; height:34px; border-radius:11px; background:#eef1ff; color:#4b5ee0; font-size:16px;}
    .score-value {color:#182447; font-size:31px; line-height:1.1; font-weight:850; letter-spacing:-.04em;}
    .score-foot {margin-top:8px; color:#8791a4; font-size:12px;}
    .mini-track {height:6px; overflow:hidden; margin-top:15px; border-radius:99px; background:#edf0f7;}
    .mini-fill {height:100%; border-radius:99px; background:linear-gradient(90deg,#4263eb,#8b5cf6);}

    .result-card {
        height:100%; padding:22px; border:1px solid var(--line); border-radius:18px;
        background:#fff; box-shadow:0 8px 24px rgba(25,40,80,.04);
    }
    .result-card-title {display:flex; align-items:center; gap:9px; margin-bottom:7px; color:#192544; font-size:16px; font-weight:800;}
    .result-card-sub {margin-bottom:17px; color:#8490a5; font-size:12px;}
    .skill-badge {display:inline-block; margin:0 6px 7px 0; padding:7px 10px; border-radius:9px; font-size:12px; font-weight:700;}
    .badge-green {color:#087b58; background:#eafaf3; border:1px solid #c9f0df;}
    .badge-red {color:#b54747; background:#fff0f0; border:1px solid #ffd8d8;}
    .badge-blue {color:#4054c5; background:#eef1ff; border:1px solid #dce2ff;}
    .empty-note {color:#8791a4; font-size:13px;}

    .recommendation {
        display:flex; align-items:flex-start; gap:12px;
        padding:15px 17px; margin-bottom:10px;
        border:1px solid #e6eafb; border-radius:13px; background:#fff;
        color:#43506a; font-size:13px; line-height:1.6;
    }
    .recommendation-icon {flex:0 0 28px; display:flex; align-items:center; justify-content:center; width:28px; height:28px; border-radius:9px; color:#4a5de0; background:#eef1ff; font-weight:800;}

    .method-note {
        padding:13px 15px; margin-top:18px; border-radius:12px;
        background:#f0f4ff; color:#56658d; font-size:12px; line-height:1.65;
    }
    .footer {
        margin-top:48px; padding-top:20px; border-top:1px solid #e5e9f2;
        color:#929caf; text-align:center; font-size:12px;
    }

    @media (max-width: 850px) {
        .hero-wrap {grid-template-columns:1fr; padding:2rem 1.5rem;}
        .hero-art {display:none;}
        .hero-title {font-size:2.4rem;}
        .results-banner {align-items:flex-start; flex-direction:column;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# ANALYSIS FUNCTIONS
# =========================================================
SKILLS = [
    "Machine Learning", "Artificial Intelligence", "Deep Learning",
    "Scikit-learn", "TensorFlow", "JavaScript", "Power BI",
    "Streamlit", "GitHub", "PyTorch", "Pandas", "NumPy", "Python",
    "TensorFlow", "Keras", "NLP", "SQL", "HTML", "CSS", "React",
    "Docker", "AWS", "Excel", "Git",
]


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    pages_text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            pages_text.append(page_text)
    return "\n".join(pages_text)


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def extract_skills(text):
    found = []
    text_lower = text.lower()
    for skill in dict.fromkeys(SKILLS):
        # Match whole words/phrases to avoid accidental substring matches.
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, text_lower):
            found.append(skill)
    return found


def calculate_similarity(resume_text, job_description):
    if not resume_text.strip() or not job_description.strip():
        return 0.0
    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        matrix = vectorizer.fit_transform([resume_text, job_description])
        return float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100)
    except ValueError:
        return 0.0


def calculate_skill_match(resume_skills, job_skills):
    if not job_skills:
        return 0.0
    return len(set(resume_skills) & set(job_skills)) / len(set(job_skills)) * 100


def generate_recommendations(missing_skills):
    recommendations = {
        "Python": "Improve Python programming, debugging, and problem-solving through practical exercises.",
        "Machine Learning": "Practice core ML algorithms and complete end-to-end projects with model evaluation.",
        "Deep Learning": "Learn neural networks and build a small deep-learning project.",
        "Artificial Intelligence": "Strengthen AI fundamentals and explore practical AI applications.",
        "NLP": "Practice text preprocessing, TF-IDF, embeddings, and NLP model evaluation.",
        "Pandas": "Practice data cleaning, grouping, joins, and exploratory data analysis with pandas.",
        "NumPy": "Practice numerical computing, arrays, indexing, and vectorized operations.",
        "Scikit-learn": "Build reusable ML pipelines with preprocessing, cross-validation, and metrics.",
        "TensorFlow": "Learn TensorFlow fundamentals and train a simple neural network.",
        "Keras": "Practice creating, training, and evaluating neural networks using Keras.",
        "PyTorch": "Learn tensors, autograd, and a basic PyTorch training loop.",
        "SQL": "Practice SELECT queries, joins, filtering, grouping, and subqueries.",
        "HTML": "Improve semantic HTML and accessible page structure.",
        "CSS": "Practice responsive layouts, Flexbox, Grid, and reusable styling.",
        "JavaScript": "Strengthen JavaScript fundamentals, functions, arrays, and DOM manipulation.",
        "React": "Learn components, props, state, hooks, and API integration.",
        "Streamlit": "Build interactive data apps with forms, charts, and clear user feedback.",
        "Git": "Practice commits, branches, merges, and version-control workflows.",
        "GitHub": "Maintain clear project READMEs and practice issues and pull requests.",
        "Docker": "Learn Docker images, containers, Dockerfiles, and application packaging.",
        "AWS": "Explore AWS fundamentals and deploy a small application to the cloud.",
        "Power BI": "Practice data modelling, measures, and interactive dashboard design.",
        "Excel": "Practice formulas, lookup functions, pivot tables, and reporting.",
    }
    return [recommendations[skill] for skill in missing_skills if skill in recommendations]


def badge_html(items, css_class, prefix=""):
    if not items:
        return '<span class="empty-note">No skills detected in this category.</span>'
    return "".join(
        f'<span class="skill-badge {css_class}">{prefix}{html.escape(skill)}</span>'
        for skill in items
    )


# =========================================================
# HERO WITH EMBEDDED ILLUSTRATION (NO EXTRA IMAGE FILE NEEDED)
# =========================================================
hero_svg = """
<svg viewBox="0 0 440 330" role="img" aria-label="Resume analysis dashboard illustration" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffffff"/><stop offset="1" stop-color="#eef2ff"/></linearGradient>
    <linearGradient id="orb" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#91a4ff"/><stop offset="1" stop-color="#bba5ff"/></linearGradient>
  </defs>
  <circle cx="235" cy="160" r="142" fill="#ffffff" opacity=".08"/>
  <circle cx="350" cy="57" r="22" fill="#9cebd8" opacity=".9"/>
  <circle cx="73" cy="250" r="13" fill="#ffc987"/>
  <path d="M70 85 C90 48 126 42 149 56" stroke="#9fb0ff" stroke-width="2" stroke-linecap="round" fill="none" opacity=".8"/>
  <rect x="92" y="34" width="206" height="262" rx="20" fill="#0c1534" opacity=".24" transform="rotate(-5 195 165)"/>
  <g transform="rotate(-5 195 165)">
    <rect x="82" y="24" width="206" height="262" rx="18" fill="url(#paper)"/>
    <rect x="101" y="45" width="44" height="44" rx="13" fill="#e6eaff"/>
    <path d="M114 56h17v23h-17z M118 62h9 M118 67h9 M118 72h6" stroke="#5369e8" stroke-width="2" fill="none" stroke-linecap="round"/>
    <rect x="156" y="51" width="91" height="8" rx="4" fill="#27345a"/>
    <rect x="156" y="65" width="70" height="5" rx="2.5" fill="#a7b0c6"/>
    <rect x="101" y="108" width="165" height="1" fill="#dce2f0"/>
    <rect x="101" y="124" width="70" height="6" rx="3" fill="#6c7a9c"/>
    <rect x="101" y="139" width="148" height="5" rx="2.5" fill="#d3d9e8"/>
    <rect x="101" y="150" width="130" height="5" rx="2.5" fill="#d3d9e8"/>
    <rect x="101" y="175" width="72" height="6" rx="3" fill="#6c7a9c"/>
    <rect x="101" y="190" width="150" height="5" rx="2.5" fill="#d3d9e8"/>
    <rect x="101" y="201" width="120" height="5" rx="2.5" fill="#d3d9e8"/>
    <rect x="101" y="226" width="55" height="22" rx="7" fill="#e8f8f1"/>
    <rect x="163" y="226" width="48" height="22" rx="7" fill="#edf0ff"/>
    <rect x="218" y="226" width="48" height="22" rx="7" fill="#fff0e3"/>
  </g>
  <g transform="translate(245 160)">
    <rect x="0" y="0" width="153" height="111" rx="17" fill="#ffffff"/>
    <text x="17" y="23" font-family="Arial,sans-serif" font-size="10" font-weight="700" fill="#68758b">RESUME MATCH</text>
    <circle cx="48" cy="63" r="25" fill="none" stroke="#e9edfa" stroke-width="8"/>
    <circle cx="48" cy="63" r="25" fill="none" stroke="#6273ed" stroke-width="8" stroke-linecap="round" stroke-dasharray="118 157" transform="rotate(-90 48 63)"/>
    <text x="48" y="67" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="800" fill="#192544">78%</text>
    <rect x="86" y="48" width="48" height="6" rx="3" fill="#dfe4f1"/>
    <rect x="86" y="48" width="37" height="6" rx="3" fill="#56c5a3"/>
    <rect x="86" y="61" width="48" height="6" rx="3" fill="#dfe4f1"/>
    <rect x="86" y="61" width="28" height="6" rx="3" fill="#f0b35c"/>
    <rect x="86" y="74" width="48" height="6" rx="3" fill="#dfe4f1"/>
    <rect x="86" y="74" width="41" height="6" rx="3" fill="#8d82ef"/>
  </g>
  <g transform="translate(326 27)">
    <rect width="57" height="39" rx="12" fill="url(#orb)"/>
    <path d="M28 8l3.5 8.5L40 20l-8.5 3.5L28 32l-3.5-8.5L16 20l8.5-3.5z" fill="#fff"/>
  </g>
</svg>
"""

st.html(
    f"""
    <section class="hero-wrap">
      <div class="hero-copy">
        <div class="eyebrow">✦ Career toolkit · AI-powered insights</div>
        <h1 class="hero-title">Make your next move<br>with <span>confidence.</span></h1>
        <p class="hero-subtitle">Compare your resume with a job description, discover matching skills, and identify practical ways to strengthen your application.</p>
        <div class="hero-pills">
          <span class="hero-pill">✧ Resume insights</span>
          <span class="hero-pill">⌁ Skill matching</span>
          <span class="hero-pill">↗ Actionable tips</span>
        </div>
      </div>
      <div class="hero-art">{hero_svg}</div>
    </section>
    """
)


# =========================================================
# INPUT SECTION
# =========================================================
st.html(
    """
    <div class="section-kicker">START HERE</div>
    <div class="section-title">Let's review your application</div>
    <div class="section-description">Add your resume and the role you're interested in. We'll compare the content and highlight areas to review.</div>
    """
)

left, right = st.columns(2, gap="large")

with left:
    st.html(
        """
        <div class="input-card">
          <div class="input-card-title"><span class="icon-tile">▤</span> Your resume</div>
          <div class="input-card-desc">Upload a text-based PDF resume to extract your skills and experience.</div>
        </div>
        """
    )
    uploaded_file = st.file_uploader(
        "Resume PDF",
        type=["pdf"],
        label_visibility="collapsed",
        help="PDF format only. Scanned image-only PDFs may not contain extractable text.",
    )
    if uploaded_file:
        st.caption(f"📎 Selected file: {uploaded_file.name}")

with right:
    st.html(
        """
        <div class="input-card">
          <div class="input-card-title"><span class="icon-tile">▧</span> Job description</div>
          <div class="input-card-desc">Paste the responsibilities, qualifications, and skills from the job posting.</div>
        </div>
        """
    )
    job_description = st.text_area(
        "Job description text",
        height=170,
        placeholder="Paste the complete job description here...\n\nExample: We are looking for a Python developer with machine learning, SQL, and data analysis experience.",
        label_visibility="collapsed",
    )

st.write("")
analyze = st.button("✦  Analyze my resume", type="primary", use_container_width=True)


# =========================================================
# ANALYZE + RESULTS
# =========================================================
if analyze:
    if uploaded_file is None:
        st.warning("Please upload your resume as a PDF first.")
    elif not job_description.strip():
        st.warning("Please paste the job description before starting the analysis.")
    else:
        try:
            with st.spinner("Reviewing your resume and comparing the job requirements..."):
                resume_text = extract_text_from_pdf(uploaded_file)
                cleaned_resume = clean_text(resume_text)
                cleaned_job = clean_text(job_description)

                if not cleaned_resume:
                    st.error("We couldn't extract readable text from this PDF. Try exporting your resume as a text-based PDF and upload it again.")
                    st.stop()

                resume_skills = extract_skills(cleaned_resume)
                job_skills = extract_skills(cleaned_job)
                resume_skill_set = set(resume_skills)
                job_skill_set = set(job_skills)

                matched_skills = [skill for skill in job_skills if skill in resume_skill_set]
                missing_skills = [skill for skill in job_skills if skill not in resume_skill_set]

                text_score = calculate_similarity(cleaned_resume, cleaned_job)
                skill_score = calculate_skill_match(resume_skills, job_skills)
                overall_score = (text_score * 0.40) + (skill_score * 0.60)
                recommendations = generate_recommendations(missing_skills)

            st.write("")
            st.html(
                f"""
                <div class="results-banner">
                  <div>
                    <div class="results-title">Your resume insights</div>
                    <div class="results-subtitle">Analysis complete for <strong>{html.escape(uploaded_file.name)}</strong></div>
                  </div>
                  <div class="status-chip">✓ Analysis complete</div>
                </div>
                """
            )

            st.html(
                """
                <div class="section-kicker">THE OVERVIEW</div>
                <div class="section-title">Your match at a glance</div>
                <div class="section-description">Use these scores as guidance for reviewing your application—not as a hiring decision.</div>
                """
            )

            metrics = [
                ("Overall match", overall_score, "◉", "Weighted score · 40% text + 60% skills"),
                ("Text similarity", text_score, "⌁", "Similarity of wording and context"),
                ("Skill match", skill_score, "✳", f"{len(matched_skills)} of {len(job_skills)} detected job skills matched" if job_skills else "No supported skills detected in job text"),
            ]
            metric_cols = st.columns(3, gap="medium")
            for col, (label, score, icon, foot) in zip(metric_cols, metrics):
                safe_score = max(0.0, min(100.0, score))
                with col:
                    st.html(
                        f"""
                        <div class="score-card">
                          <div class="score-top"><div class="score-label">{label}</div><div class="score-icon">{icon}</div></div>
                          <div class="score-value">{score:.1f}<span style="font-size:18px;color:#8791a4">%</span></div>
                          <div class="mini-track"><div class="mini-fill" style="width:{safe_score:.2f}%"></div></div>
                          <div class="score-foot">{foot}</div>
                        </div>
                        """
                    )

            st.write("")
            skills_left, skills_right = st.columns(2, gap="large")

            with skills_left:
                st.html(
                    f"""
                    <div class="result-card">
                      <div class="result-card-title">🟢 Matching skills</div>
                      <div class="result-card-sub">Skills detected in both your resume and the job description.</div>
                      {badge_html(matched_skills, 'badge-green', '✓ ')}
                    </div>
                    """
                )
            with skills_right:
                st.html(
                    f"""
                    <div class="result-card">
                      <div class="result-card-title">🟠 Skills to review</div>
                      <div class="result-card-sub">Skills mentioned in the job description but not detected in your resume.</div>
                      {badge_html(missing_skills, 'badge-red', '+ ')}
                    </div>
                    """
                )

            st.write("")
            st.html(
                f"""
                <div class="result-card">
                  <div class="result-card-title">✧ Skills found in your resume</div>
                  <div class="result-card-sub">These are skills recognized by the app's current keyword list.</div>
                  {badge_html(resume_skills, 'badge-blue')}
                </div>
                """
            )

            st.write("")
            st.html(
                """
                <div class="section-kicker">NEXT STEPS</div>
                <div class="section-title">Ways to strengthen your application</div>
                <div class="section-description">Consider these suggestions when they are relevant to your actual experience and career goals.</div>
                """
            )

            if recommendations:
                for index, recommendation in enumerate(recommendations, start=1):
                    st.html(
                        f"""
                        <div class="recommendation">
                          <div class="recommendation-icon">{index:02d}</div>
                          <div>{html.escape(recommendation)}</div>
                        </div>
                        """
                    )
            else:
                st.success("No missing skills were detected from the app's current keyword list. Review the full job description to make sure all important requirements are covered.")

            st.html(
                """
                <div class="method-note"><strong>How to interpret these results:</strong> This is a keyword-based prototype using TF-IDF cosine similarity and a predefined skills list. It can miss synonyms, context, or skills that are described differently. A score is not a prediction of whether an employer will interview or hire you.</div>
                """
            )

        except Exception as error:
            st.error(f"Something went wrong while analyzing this file: {error}")


# =========================================================
# FOOTER
# =========================================================
st.html(
    """
    <div class="footer">AI Resume Analyzer <span style="padding:0 7px">·</span> Built with Python, NLP & Streamlit<br><span style="display:inline-block;margin-top:6px">A portfolio project for resume-to-job-description analysis</span></div>
    """
)
