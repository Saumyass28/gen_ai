# app.py
import streamlit as st
from qa_bot import qa_bot  # Import the QA bot function

st.title("Interactive QA Bot")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
user_query = st.text_input("Ask a question")

if st.button("Submit"):
    if uploaded_file is not None and user_query:
        answer, document_segments = qa_bot(user_query, uploaded_file)
        st.write(f"**Answer:** {answer}")
        st.write(f"**Document Segments:** {document_segments}")
    else:
        st.warning("Please upload a PDF and enter a question.")
