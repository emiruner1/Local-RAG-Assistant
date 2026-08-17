from openai import OpenAI

from config import CHAT_MODEL


client = OpenAI(
    base_url="http://127.0.0.1:65228/v1",
    api_key="unused"
)


def ask_llm(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer using ONLY the context below.

If possible, summarize the context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content