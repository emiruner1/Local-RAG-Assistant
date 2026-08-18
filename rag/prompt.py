def build_rag_prompt(question, context):
    return f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the provided context.

Rules:
- Do not use information that is not in the context.
- If the answer cannot be found in the context, say:
  "I couldn't find the answer in the provided documents."
- Give a clear and concise answer.
- Do not invent facts.

Context:
{context}

Question:
{question}

Answer:
"""
