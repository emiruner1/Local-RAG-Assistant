import json

from openai import OpenAI

from config import EMBEDDING_MODEL


client = OpenAI(
    base_url="http://127.0.0.1:65228/v1",
    api_key="unused"
)


def create_embedding(text):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding


def embedding_to_json(vector):
    return json.dumps(vector)


def json_to_embedding(text):
    return json.loads(text)