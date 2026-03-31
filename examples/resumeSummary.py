import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.extractor import extract_text_from_pdf, extract_entities
from app.summarizer import resumeSummary
from app.tokenizer import count_tokens

resume_text = extract_text_from_pdf("resume.pdf")

summary = resumeSummary(resume_text)
entities = extract_entities(resume_text)

print("\nCONTENT PREVIEW:\n", resume_text[:500])
print("\nSUMMARY:\n", summary)
print("\nEXTRACTION:\n", entities)
print("Token count:", count_tokens(resume_text))
tokens = count_tokens(resume_text)