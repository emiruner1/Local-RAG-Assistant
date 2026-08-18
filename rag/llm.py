from foundry_local_sdk import Configuration, FoundryLocalManager

from config import CHAT_MODEL
from rag.prompt import build_rag_prompt


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
    prompt = build_rag_prompt(question, context)

    response = client.complete_chat(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
