import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def show():
    st.title("Text to Graph")
    st.write("This page generates a word cloud from the provided text.")

    text = st.text_area("Enter text for word cloud", height=200)
    if st.button("Generate Word Cloud"):
        wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="Blues").generate(text)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
