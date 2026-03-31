from app.extractor import extract_entities
from app.scraper import fetch_website_contents
from app.summarizer import summarize


def content_format(url: str, summary_style: str = "bullet", verify_ssl: bool = True) -> dict:
    content = fetch_website_contents(url, verify_ssl=verify_ssl)
    return {
        "url": url,
        "content": content,
        "summary": summarize(content, style=summary_style),
        "entities": extract_entities(content),
    }
