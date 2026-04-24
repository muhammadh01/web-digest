"""
main.py
-------
Command-line entry point for web-digest.

Usage:
    python main.py <url>

Example:
    python main.py https://anthropic.com
"""

import sys

from summarizer import summarize


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        print("Example: python main.py https://anthropic.com")
        return 1

    url = sys.argv[1]
    print(f"Fetching and summarizing: {url}\n")

    try:
        summary = summarize(url)
    except Exception as exc:
        print(f"Error: {exc}")
        return 1

    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
