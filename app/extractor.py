import json
import pdfplumber
from app.llm_client import generate_response
from app.tokenizer import prepare_input

def _strip_markdown_json(response: str) -> str:
    cleaned = response.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    return cleaned


def extract_entities(text):
    text = prepare_input(text)
    system_prompt = "Extract structured data in JSON format."

    user_prompt = f"""
     {{
      "name": string,
      "headline": string,
      "about": string,
      "top_skills": [string],
      "experience": [string]
    }}

    Rules:
    - "experience" should contain only company names
    - "top_skills" should be a list of skills
    - Do not hallucinate (only use given text)
    - Return ONLY JSON (no explanation)

    Text:
    {text}
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = generate_response(messages)
    cleaned_response = _strip_markdown_json(response)

    try:
        return json.loads(cleaned_response)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON", "raw": response}

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text