from app.llm_client import generate_response
from app.tokenizer import safe_input

def classify(text):
    system_prompt = "Classify text into categories."
    text = safe_input(text, max_tokens=1200)

    user_prompt = f"""
    Classify this text into one of:
    - Technology
    - Business
    - Health
    - Other

    Text:
    {text}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return generate_response(messages)
