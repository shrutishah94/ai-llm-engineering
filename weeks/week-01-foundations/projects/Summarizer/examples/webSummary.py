import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.orchestration.pipeline import content_format

url = "https://www.linkedin.com/in/shruti189/?skipRedirect=true"
result = content_format(url)

print("URL:\n", result["url"])
print("\nSCRAPED CONTENT PREVIEW:\n", result["content"][:500], "...")
print("\nSUMMARY:\n", result["summary"])
print("\nEXTRACTION:\n", result["entities"])
