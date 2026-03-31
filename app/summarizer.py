#For Text Summary
from app.llm_client import generate_response
from app.tokenizer import safe_input

def summarize(text, style="bullet"):
    text = safe_input(text, max_tokens=1200)

    system_prompt = "You are a helpful assistant that summarizes text."
   
    user_prompt = f"""
    Summarize the following text in {style} format:

    {text}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return generate_response(messages)

def resumeSummary(text, style="bullet"):
    text = safe_input(text, max_tokens=1200)
    system_prompt = "You are a helpful reader that summarizes content."
    user_prompt = f"""
    Summarize the document in {style} format:

    {text}
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return generate_response(messages)
