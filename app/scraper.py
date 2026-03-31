#For Web scrapping
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

# Standard headers to fetch a website
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid URL: {url!r}. Use a full http/https URL.")


def fetch_website_contents(
    url: str, max_chars: int = 2000, timeout: int = 15, verify_ssl: bool = True
) -> str:
    """
    Return title + cleaned body text for the given URL
    """
    _validate_url(url)
    response = requests.get(url, headers=HEADERS, timeout=timeout, verify=verify_ssl)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"

    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    return (title + "\n\n" + text)[:max_chars]


def fetch_website_links(url: str, timeout: int = 15, verify_ssl: bool = True) -> list[str]:
    """
    Return relative links found on the page
    """
    _validate_url(url)
    response = requests.get(url, headers=HEADERS, timeout=timeout, verify=verify_ssl)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]
