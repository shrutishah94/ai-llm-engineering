from app.llm_client import generate_response
from app.tokenizer import prepare_input

def rewrite(text, tone="professional"):
    text = prepare_input(text)
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
