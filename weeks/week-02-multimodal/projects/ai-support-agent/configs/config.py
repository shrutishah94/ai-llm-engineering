import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")

gpt_client = OpenAI(api_key=OPENAI_API_KEY)
ollama_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key=OLLAMA_API_KEY,
)

gpt_model = "gpt-4.1-mini"
ollama_model = "llama3.2"

gpt_prompt = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

ollama_prompt = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."