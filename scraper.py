import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


def fetch_website_contents(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    for tag in soup(["script", "style", "img", "input", "nav", "footer"]):
        tag.decompose()

    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"
    body_text = soup.body.get_text(separator="\n", strip=True) if soup.body else ""

    return f"{title}\n\n{body_text}"
