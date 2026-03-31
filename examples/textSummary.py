import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.classifier import classify
from app.extractor import extract_entities
from app.rewriter import rewrite
from app.summarizer import summarize

text = "OpenAI released new AI models that are transforming industries."

print("SUMMARY:\n", summarize(text))
print("\nEXTRACTION:\n", extract_entities(text))
print("\nCLASSIFICATION:\n", classify(text))
print("\nREWRITE:\n", rewrite(text, tone="casual"))
