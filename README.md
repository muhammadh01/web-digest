# web-digest

A tiny Python tool that fetches any web page and produces a short, clean summary using an OpenAI model. Give it a URL, get the Reader's Digest version back.

## Features

- Scrapes visible text from a web page (strips scripts, styles, nav, etc.)
- Sends the cleaned text to an OpenAI chat model
- Returns a markdown summary, including any news or announcements

## Setup

1. Clone the repo and enter it:
   ```bash
   git clone https://github.com/<your-username>/web-digest.git
   cd web-digest
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key:
   ```bash
   cp .env.example .env
   # then edit .env and paste your real key
   ```

## Usage

```bash
python main.py https://anthropic.com
```

You'll get back a markdown summary of the page printed to the terminal.

## Project structure

```
web-digest/
├── main.py            # CLI entry point
├── summarizer.py      # OpenAI logic + prompts
├── scraper.py         # Fetch and clean website HTML
├── requirements.txt
├── .env.example
└── .gitignore
```

## Notes

- Works on static sites. Pages rendered by JavaScript (React/Vue SPAs) may not scrape well — a future version could add Selenium or Playwright.
- Cost is tiny: `gpt-4.1-mini` is cheap, and each call is one short request.

## License

MIT
