import json

from foundry_local_sdk import Configuration, FoundryLocalManager

from config import EMBEDDING_MODEL


# Initialize Foundry Local
FoundryLocalManager.initialize(
    Configuration(app_name="local-rag-assistant")
)

manager = FoundryLocalManager.instance

# Get and load the embedding model
model = manager.catalog.get_model(EMBEDDING_MODEL)
model.load()

# Create the embedding client
client = model.get_embedding_client()


def create_embedding(text):
    response = client.generate_embedding(text)

    return response.data[0].embedding


def embedding_to_json(vector):
    return json.dumps(vector)


def json_to_embedding(text):
    return json.loads(text)
