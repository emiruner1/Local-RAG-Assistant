from foundry_local_sdk import Configuration, FoundryLocalManager

from config import CHAT_MODEL


# Initialize Foundry Local
FoundryLocalManager.initialize(
    Configuration(app_name="local-rag-assistant")
)

manager = FoundryLocalManager.instance

# Get and load the chat model
model = manager.catalog.get_model(CHAT_MODEL)
model.load()

# Create chat client
client = model.get_chat_client()


def ask_llm(question, context):
    prompt = f"""
You are a helpful AI assistant.

Answer using ONLY the context below.

If the answer cannot be found in the context, say that you don't know.

Context:
{context}

Question:
{question}
"""

    response = client.complete_chat(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
