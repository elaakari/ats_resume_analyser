# 📄 Resume Analyzer AI (ATS + Gemini AI)

## 🚀 Overview
Resume Analyzer AI is a Flask-based web application that uses Google Gemini AI to analyze resumes against job descriptions. It performs deep ATS-style analysis, evaluates CV quality, and provides professional career recommendations.

The system simulates a real Applicant Tracking System (ATS) used by companies to screen candidates.

---

## 🎯 Features
- Upload resume (PDF format)
- Extract text from CV using PyMuPDF
- AI-powered analysis using Google Gemini
- ATS compatibility scoring
- Job description parsing
- Skills vs requirements matching
- Missing skills detection
- Strengths and weaknesses identification
- Keyword gap analysis
- Personalized recommendations
- Structured professional report

---

## 🧠 AI Capabilities

The system analyzes:

### 📌 Job Description
- Job Title
- Seniority Level
- Industry
- Hard Skills
- Soft Skills
- Technologies
- Certifications
- Responsibilities
- Keywords

### 📌 Resume Analysis
- Professional summary quality
- Experience relevance
- Education matching
- Skills extraction
- Projects evaluation
- Grammar and clarity

### 📌 ATS Analysis
- Column structure detection
- Tables / icons / images detection
- ATS compatibility scoring
- Formatting issues

---

## 🛠️ Tech Stack
- Python
- Flask
- Google Gemini API
- PyMuPDF (fitz)
- HTML / CSS
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```
│   .gitignore
│   analyse_pdf.py
│   main.py
│   requirement.txt
│
├───Templates
│       index.html
│
└───__pycache__
        analyse_pdf.cpython-314.pyc


```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000
```

---

## 📊 Output Report Includes

- Match Score (0–100)
- ATS Score
- Skills Match Score
- Experience Score
- Missing Skills
- Strengths
- Weaknesses
- ATS Issues
- Visual Issues
- Keyword Gaps
- Recommendations
- Detailed AI Explanation

---

## 📌 Use Cases

- Job seekers optimizing CVs
- ATS simulation system
- HR recruitment screening
- Career coaching tool
- Data/AI portfolio project

---

## ⚠️ Security Notes

- `.env` is excluded using `.gitignore`
- API keys must NEVER be pushed to GitHub
- Use `.env.example` for sharing structure


