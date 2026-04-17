import pandas as pd
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess(reviews):
    df = pd.DataFrame(reviews)
    df.drop_duplicates(subset=["title"], inplace=True)
    df["cleaned_review"] = df["review"].apply(clean_text)
    return df

if __name__ == "__main__":
    sample = [
        {"title": "Book One", "rating": "Three", "price": "£12.99", "review": "This book is rated Three stars and priced at £12.99."},
        {"title": "Book Two", "rating": "Five", "price": "£9.99", "review": "This book is rated Five stars and priced at £9.99."},
    ]
    df = preprocess(sample)
    print(df)
    