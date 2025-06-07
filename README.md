# 📄 Resume Analyzer

A simple resume analysis tool built using Python, NLP (spaCy), PDF parsing (PyMuPDF), and Streamlit. This app allows users to upload their resume in PDF format, extract key details, and receive suggestions for improvement.

---

## 🚀 Features

- Upload and parse PDF resumes
- Extract education, experience, and skills using NLP
- Generate resume improvement suggestions
- User-friendly web interface with Streamlit

---

## 📦 Tech Stack

- **Python**
- **spaCy** for NLP
- **PyMuPDF (fitz)** for PDF parsing
- **Streamlit** for the web interface

---

## 📥 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Vaishu2916/Resume-Suggestion.git
cd Resume-Suggestion
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm
🧪 Sample PDF
Place a sample resume file (e.g., sample_resume.pdf) in the root folder to test locally.

📂 Project Structure
bash
Copy
Edit
Resume-Suggestion/
├── app.py               # Streamlit frontend
├── resume_parser.py     # Resume parsing and NLP logic
├── sample_resume.pdf    # Example resume file
└── README.md
▶️ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
