import streamlit as st
import tempfile
from resume_parser import extract_text_from_pdf, extract_entities, suggest_improvements

st.title("📄 Resume Analyzer")
st.write("Upload your resume in PDF format and get suggestions to improve it!")

uploaded_file = st.file_uploader("Choose a resume PDF", type="pdf")

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.success("Resume uploaded successfully!")

    text = extract_text_from_pdf(tmp_path)
    st.subheader("Extracted Text")
    st.text_area("Raw Resume Text", text, height=200)

    entities = extract_entities(text)
    st.subheader("Detected Details")
    st.write(entities)

    suggestions = suggest_improvements(entities)
    st.subheader("Suggestions")
    if suggestions:
        for s in suggestions:
            st.warning(s)
    else:
        st.success("Your resume looks great!")
