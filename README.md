# Product Review Analyzer

A Python application that scrapes book data from [books.toscrape.com](https://books.toscrape.com/catalogue/page-1.html), cleans the text, analyzes sentiment using Groq LLM, and stores results in CSV.

## Chosen Product URL
https://books.toscrape.com/catalogue/page-1.html

## Tech Stack
- Python
- requests, BeautifulSoup
- pandas
- Groq API (llama3-70b-8192)
- python-dotenv
- tiktoken

## Setup

1. Clone the repo:
git clone https://github.com/choudhary09srishti-boop/product-review-analyzer-.git
cd product-review-analyzer-

2. Create virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create `.env` file:
GROQ_API_KEY=your_key_here

5. Run:
python main.py

## Output
Results saved to `data/output.csv` with columns:
- `title` — book title
- `rating` — star rating
- `price` — book price
- `review` — raw generated review text
- `cleaned_review` — preprocessed text
- `sentiment` — Positive / Negative / Neutral
- `summary` — one sentence summary
- `key_themes` — comma separated themes

## Design Choices
- Used books.toscrape.com as it is a legal, bot-friendly scraping practice site
- Groq API used as OpenAI-compatible LLM provider
- Reviews are cleaned using regex before sending to LLM
- Rate limit handling via try/except with 5 second retry delay
- Data stored in CSV using pandas

## Limitations
- books.toscrape.com does not have real customer reviews; review text is synthetically generated from rating and price
- LLM output quality depends on Groq API availability
- No pagination beyond max_pages limit
- No token counting implemented beyond basic chunking