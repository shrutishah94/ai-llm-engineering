import os

from dotenv import load_dotenv
from openai import OpenAI
from app.config import MAX_OUTPUT_TOKENS

load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is missing")

client = OpenAI(api_key=api_key)

def generate_response(messages, temperature=0.3):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        #Output tokens layer
        max_tokens=MAX_OUTPUT_TOKENS,
    )
    print("Input tokens:", response.usage.prompt_tokens)
    print("Output tokens:", response.usage.completion_tokens)
    print("Total tokens:", response.usage.total_tokens)

    return response.choices[0].message.content