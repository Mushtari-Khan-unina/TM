import streamlit as st
import PyPDF2
from transformers import pipeline

def show():
    st.title("PDF Summarizer")
    st.write("This page summarizes text from a PDF document.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
        text = ""
        for page in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page).extract_text()

        if st.button("Summarize"):
            summarizer = pipeline("summarization")
            summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
            st.write("Summary:", summary[0]['summary_text'])
