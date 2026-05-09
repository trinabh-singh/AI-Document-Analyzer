import pdfplumber
import re
from langchain_text_splitters import RecursiveCharacterTextSplitter


def process_pdf(pdf_path):

    documents = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_number, page in enumerate(pdf.pages, start=1):

            text = page.extract_text(layout=True)

            if text:

                documents.append({
                    "page": page_number,
                    "content": text.strip()
                })

    def clean_text(text):

        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\x00-\x7f]', '', text)

        return text.strip()

    for doc in documents:
        doc["content"] = clean_text(doc["content"])

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    final_chunks = []

    for doc in documents:

        chunks = text_splitter.split_text(doc["content"])

        for chunk in chunks:

            final_chunks.append({
                "metadata": {"page": doc["page"]},
                "content": chunk
            })

    return final_chunks