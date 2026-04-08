from app.models.llm_client import generate_response
from app.tools.tokenizer import prepare_input


def classify(text):
    system_prompt = "Classify text into categories."
    text = prepare_input(text)

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
