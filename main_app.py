import streamlit as st
from streamlit.components.v1 import html

# Custom CSS for the entire app
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation bar
def navbar():
    st.markdown(
        """
        <div class="navbar">
            <a href="?page=Home">Home</a>
            <a href="?page=About">About</a>
            <a href="?page=LLM_Summarizer">LLM Summarizer</a>
            <a href="?page=PDF_Summarizer">PDF Summarizer</a>
            <a href="?page=Text_to_Graph">Text to Graph</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Page content loader
def load_page(page):
    if page == "Home":
        st.title("Home Page")
        st.write("Welcome to the Home Page.")
    elif page == "About":
        import pages.about
        pages.about.show()
    elif page == "LLM Summarizer":
        import pages.llm_summarizer
        pages.llm_summarizer.show()
    elif page == "PDF Summarizer":
        import pages.pdf_summarizer
        pages.pdf_summarizer.show()
    elif page == "Text to Graph":
        import pages.text_to_graph
        pages.text_to_graph.show()

def main():
    load_css()
    navbar()
    
    page = st.experimental_get_query_params().get("page", ["Home"])[0]
    load_page(page)

if __name__ == "__main__":
    main()
