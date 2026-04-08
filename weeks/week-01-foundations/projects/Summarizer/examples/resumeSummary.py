import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))

file_path = BASE_DIR.parent / "data" / "Shruti Shah Resume.pdf"

from app.tools.extractor import extract_entities, extract_text_from_pdf
from app.tools.summarizer import resumeSummary

resume_text = extract_text_from_pdf(str(file_path))

summary = resumeSummary(resume_text)
entities = extract_entities(resume_text)

#print("\nCONTENT:\n", resume_text)
print("\nSUMMARY:\n", summary)
print("\nEXTRACTION:\n", entities)
