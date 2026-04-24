import os
from dotenv import load_dotenv
from openai import OpenAI

from scraper import fetch_website_contents

load_dotenv(override=True)

SYSTEM_PROMPT = """
You are an assistant that analyzes the contents of a website
and provides a short, clear summary, ignoring navigation-related text.
If the site contains news or announcements, summarize those too.
Respond in markdown. Do not wrap the markdown in a code block.
"""

USER_PROMPT_PREFIX = (
    "Here are the contents of a website. "
    "Provide a short summary of this website.\n\n"
)

MODEL = "gpt-4.1-mini"


def _build_messages(website_text):
    return [
        {"role": "system", "content": SYSTEM_PROMPT.strip()},
        {"role": "user", "content": USER_PROMPT_PREFIX + website_text},
    ]


def summarize(url):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY not found. Copy .env.example to .env and add your key."
        )

    client = OpenAI(api_key=api_key)

    website_text = fetch_website_contents(url)
    response = client.chat.completions.create(
        model=MODEL,
        messages=_build_messages(website_text),
    )
    return response.choices[0].message.content
