import pandas as pd
import os
from scraper import scrape_books
from preprocess import preprocess
from llm import analyze_review, parse_llm_output

def save_to_csv(df, path="data/output.csv"):
    os.makedirs("data", exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved to {path}")

def main():
    url = "https://books.toscrape.com/catalogue/page-1.html"
    max_pages = 3

    print("Step 1: Scraping...")
    raw_data = scrape_books(url, max_pages=max_pages)
    print(f"Scraped {len(raw_data)} books.")

    print("Step 2: Preprocessing...")
    df = preprocess(raw_data)
    print(f"After cleaning: {len(df)} records.")

    print("Step 3: Analyzing with LLM...")
    sentiments = []
    summaries = []
    themes = []

    for i, row in df.iterrows():
        print(f"Analyzing {i+1}/{len(df)}: {row['title'][:40]}...")
        output = analyze_review(row["cleaned_review"])
        parsed = parse_llm_output(output)
        sentiments.append(parsed["sentiment"])
        summaries.append(parsed["summary"])
        themes.append(parsed["key_themes"])

    df["sentiment"] = sentiments
    df["summary"] = summaries
    df["key_themes"] = themes

    print("Step 4: Saving...")
    save_to_csv(df)
    print("Done.")

if __name__ == "__main__":
    main()