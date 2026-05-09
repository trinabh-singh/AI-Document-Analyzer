from openai import OpenAI
from dotenv import load_dotenv
import os
from pdftext import process_pdf
from embeding import create_vector_store , embedding_model



load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

current_chunks = None
current_index = None


def load_pdf(pdf_path):

    global current_chunks
    global current_index

    current_chunks = process_pdf(pdf_path)

    current_index = create_vector_store(
        current_chunks
    )

def retrieve_relevant_chunks(query, model, index, chunks, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks

def build_prompt(question, context_chunks):

    context = "\n\n".join(
        [chunk["content"] for chunk in context_chunks]
    )


    prompt = f"""
You are a helpful AI assistant.

Use the provided context to answer the user's question in a natural, conversational, and professional way.

Do not copy the context word-for-word unless necessary.

If the answer is not present in the context, say:
"I could not find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt


def generate_answer(prompt):

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
   
    return response.choices[0].message.content


def ask_question(question):

    retrieved_chunks = retrieve_relevant_chunks(
        question,
        embedding_model,
        current_index,
        current_chunks
    )

    prompt = build_prompt(
        question,
        retrieved_chunks
    )
    
    answer = generate_answer(prompt)

    return answer
