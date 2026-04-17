# Product Review Analyzer

A Python app that scrapes book data from books.toscrape.com, cleans the text, analyzes sentiment using Groq LLM, and stores results in CSV.

## Tech Stack
- Python
- requests, BeautifulSoup
- pandas
- Groq API
- python-dotenv
- tiktoken

## Setup

1. Clone the repo
2. Create virtual environment:
3. Install dependencies:
4. Create `.env` file:
5. Run:

## Output
Results saved to `data/output.csv` with columns:
- title, rating, price, review, cleaned_review, sentiment, summary, key_themes