import streamlit as st
from transformers import pipeline

def show():
    st.title("LLM Text Summarizer")
    st.write("This page summarizes text using a language model.")

    text = st.text_area("Enter text to summarize", height=200)
    if st.button("Summarize"):
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        st.write("Summary:", summary[0]['summary_text'])
