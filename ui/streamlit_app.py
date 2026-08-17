import time
import streamlit as st

from database.sqlite_manager import (
    create_table,
    delete_database,
    document_list,
    chunk_count,
)
from rag.ingest import ingest
from rag.retrieval import retrieve
from rag.llm import ask_llm

create_table()

st.set_page_config(
    page_title="Local RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Local RAG Assistant")
st.caption("🚀 Offline AI • RAG • Foundry Local • Phi-4 Mini • SQLite")

with st.sidebar:

    st.header("📄 Knowledge Base")

    pdf = st.file_uploader("Upload PDF", type=["pdf"])

    if pdf:

        with open(f"data/documents/{pdf.name}", "wb") as f:
            f.write(pdf.getbuffer())

        if st.button("Index PDF"):

            with st.spinner("Creating embeddings..."):
                ingest(f"data/documents/{pdf.name}")

            st.success("PDF indexed!")

    st.divider()

    st.subheader("📚 Indexed Documents")

    for doc in document_list():
        st.write(f"📄 {doc}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Documents", len(document_list()))

    with col2:
        st.metric("Chunks", chunk_count())

    if st.button("🗑 Clear Database"):
        delete_database()
        st.success("Database cleared")
        st.rerun()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("⚙ System")
    st.write("Chat Model: Phi-4 Mini")
    st.write("Embedding: Qwen3")
    st.write("Database: SQLite")
    st.write("Runtime: Foundry Local")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask a question about your documents...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    start = time.perf_counter()

    with st.spinner("🤖 Thinking..."):

        results = retrieve(question)

        context = "\n\n".join([r[2] for r in results])

        answer = ask_llm(question, context)

    elapsed = time.perf_counter() - start

    with st.chat_message("assistant"):

        st.markdown(answer)
        st.caption(f"⏱ {elapsed:.2f} sec")

        with st.expander("📚 Sources"):

            for _, source, chunk in results:

                st.success(f"📄 {source}")

                with st.popover("View Chunk"):
                    st.write(chunk[:1000])

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
