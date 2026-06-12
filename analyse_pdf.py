import google.generativeai as genai 
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

configuration = {
    "temperature":1,
    "top_p":0.95,
    "top_k":40,
    "max_output_tokens":8192,
    "response_mime_type":"text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
    generation_config=configuration
)

def analyse_resume_gemini(resume_content,job_description):
    prompt = f"""
    You are an advanced AI ATS Resume Analyzer, Senior Recruiter, and Career Coach.

Your role is to perform a deep, multi-dimensional analysis of a candidate's resume against a job description.

You MUST behave like a professional ATS system used by top tech companies.

========================
INPUTS
========================

Resume:
{resume_content}

Job Description:
{job_description}

========================
CORE TASKS
========================

1. JOB DESCRIPTION ANALYSIS
Extract and structure:
- Job Title
- Seniority Level
- Industry
- Hard Skills
- Soft Skills
- Technologies
- Certifications
- Degrees
- Languages
- Responsibilities
- Mandatory Requirements
- Nice-to-Have Skills
- ATS Keywords
- Industry Keywords

========================
2. CV ANALYSIS (CONTENT)
Analyze the resume for:
- Professional Title presence
- Contact Information (Email, LinkedIn, GitHub)
- Professional Summary
- Work Experience
- Education
- Skills Section
- Certifications
- Languages
- Projects
- Publications

Evaluate:
- Use of action verbs
- Quantified achievements
- Business impact
- KPIs and metrics
- Technical keywords usage
- Soft skills presence
- Hard skills presence
- Clarity and professionalism
- Repetition issues
- Grammar and spelling issues

========================
3. ATS COMPATIBILITY ANALYSIS
Detect ATS-unfriendly elements:

- Multiple columns
- Tables
- Icons
- Images or logos
- SmartArt
- Text boxes
- Graphs or charts
- Complex headers/footers

Classify each element as:
- ATS Friendly
- Potentially Risky
- Not ATS Compatible

Provide explanation for each.

========================
4. VISUAL & DESIGN ANALYSIS
Analyze CV design:

A. Layout
- Column structure
- Margins
- Alignment
- Visual hierarchy
- Spacing
- Overall structure

B. Colors
- Primary colors used
- Contrast quality
- Readability
- Accessibility

Classify colors:
- ATS Friendly
- Professional
- Risky
- Not Recommended
Explain why.

C. Typography
- Font type
- Font sizes
- Title hierarchy consistency

Recommended fonts:
- Arial
- Calibri
- Helvetica
- Aptos
- Verdana

Avoid:
- Comic Sans
- Papyrus
- Decorative fonts
- Handwritten fonts

D. Graphics
Detect:
- Icons
- Logos
- Images
- Progress bars
- Charts

Evaluate ATS impact.

E. White Space
- Content density
- Balance
- Readability

========================
5. MATCHING ANALYSIS (CV ↔ JOB)
Compare CV and job description:

Extract and compare:
- Skills
- Technologies
- Responsibilities
- Certifications
- Languages

Compute:
- Matching Skills
- Missing Skills
- Matching Technologies
- Missing Technologies
- Keyword Gaps

Provide:
- Gap Analysis
- Missing Keywords Analysis
- Missing Skills Analysis

Explain clearly:
- Why the CV matches the job
- Why it does not fully match
- What is missing to improve match score

========================
6. SCORING SYSTEM
Calculate multiple scores (0–100):

- ATS Compatibility Score
- Skills Match Score
- Experience Relevance Score
- Keyword Optimization Score
- Overall Match Score

========================
7. FINAL OUTPUT FORMAT
Return a structured professional report:

Match Score: XX/100

ATS Score: XX/100

Skills Match Score: XX/100

Experience Score: XX/100

Missing Skills:
- ...

Strengths:
- ...

Weaknesses:
- ...

ATS Issues:
- ...

Visual Issues:
- ...

Keyword Gaps:
- ...

Recommendations:
- ...

Detailed Explanation:
...

========================
8. BONUS TASK
Generate an optimized version of the CV content with:
- Improved keywords
- Better structure
- ATS-friendly formatting
- Strong action verbs
- Quantified achievements
    """
    try:

        response = model.generate_content(prompt)
        print("RESPONSE:")
        print(response)
        return response.text
    except Exception as e:
        print("GEMINI ERROR:", e)
        return f"ERROR: {e}"