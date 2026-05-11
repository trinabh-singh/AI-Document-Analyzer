import streamlit as st
import requests

st.title("PDF RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

# Process Button
if uploaded_file is not None:

    if st.button("Process PDF"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        with st.spinner("Processing PDF..."):

            response = requests.post(
                "https://ai-document-analyzer-backend-n5n2.onrender.com/upload",
                files=files
            )

        if response.status_code == 200:

            st.success("PDF processed successfully!")

            st.session_state.pdf_uploaded = True

        else:

            st.error("PDF upload failed.")

# Show chatbot ONLY after upload
if st.session_state.get("pdf_uploaded", False):

    query = st.chat_input(
        "Ask question about PDF"
    )

    if query:

        with st.chat_message("user"):
            st.write(query)

        response = requests.post(
            "https://ai-document-analyzer-backend-n5n2.onrender.com/query",
            json={"query": query}
        )

        answer = response.json()["answer"]

        with st.chat_message("assistant"):
            st.write(answer)