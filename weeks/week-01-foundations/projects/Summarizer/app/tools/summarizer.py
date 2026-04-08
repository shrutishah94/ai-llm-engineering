#For Text Summary
from app.models.llm_client import generate_response
from app.tools.tokenizer import prepare_input


def summarize(text, style="bullet"):
    text = prepare_input(text)

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
    text = prepare_input(text)
    system_prompt = """You are a smart resume analyzer.
    Rules:
    - Give information about name, location and email address 
    - Compute the total years of experience with usage of absolute from the given date ranges
    - Merge similar points
    - Do NOT explain steps unless asked
    """
    user_prompt = f"""
    Compress this resume into a concise {style} summary (max 10-15 bullets total):

    {text}
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return generate_response(messages)
