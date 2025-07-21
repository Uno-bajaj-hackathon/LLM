import streamlit as st
from app.query_parser import parse_query
from app.doc_loader import load_documents
from app.embedder import get_embeddings, load_faiss_index
from app.retriever import search_clauses
from app.llm_reasoning import evaluate_decision

st.set_page_config(page_title="LLM Document Decision System")
st.title("🧠 LLM Document Decision System")

uploaded_files = st.file_uploader("Upload policy documents", type=['pdf', 'docx', 'eml'], accept_multiple_files=True)
query = st.text_input("Enter your natural language query")

if st.button("Get Decision"):
    if uploaded_files and query:
        docs = load_documents(uploaded_files)
        chunks = [chunk for doc in docs for chunk in doc['chunks']]
        index, embeddings = get_embeddings(chunks)
        retrieved_clauses = search_clauses(query, index, embeddings, chunks)
        parsed = parse_query(query)
        result = evaluate_decision(parsed, retrieved_clauses)
        st.subheader("Result")
        st.json(result)
    else:
        st.warning("Please upload documents and enter a query.")
