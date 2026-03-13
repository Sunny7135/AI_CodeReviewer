import streamlit as st
from reviewer import review_code

st.title("AI Code Reviewer")

language = st.selectbox(
    "Select programming language",
    [
        "Python",
        "C",
        "C++",
        "Java",
        "JavaScript",
        "Go",
        "Rust",
        "TypeScript"
    ]
)

code = st.text_area("Paste your code here", height=300)

if st.button("Review Code"):

    if code.strip() == "":
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Analyzing code..."):
            result = review_code(code, language)

        st.subheader("Review Result")
        st.markdown(result)