from app.llm_client import generate_response
from app.tokenizer import safe_input

def rewrite(text, tone="professional"):
    text = safe_input(text, max_tokens=1200)
    system_prompt = "Rewrite text based on tone."

    user_prompt = f"""
    Rewrite the following text in a {tone} tone:

    {text}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return generate_response(messages)
