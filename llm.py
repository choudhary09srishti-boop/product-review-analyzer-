import os
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_review(review_text):
    prompt = f"""You are a product review analyst.
Analyze the following review and return:
1. Sentiment: (Positive / Negative / Neutral)
2. Summary: (1 sentence)
3. Key themes: (comma separated)

Review: {review_text}

Respond in this exact format:
Sentiment: ...
Summary: ...
Key themes: ...
"""
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"LLM error: {e}")
        time.sleep(5)
        return "Sentiment: Unknown\nSummary: Error\nKey themes: None"


def parse_llm_output(output):
    result = {"sentiment": "", "summary": "", "key_themes": ""}
    for line in output.split("\n"):
        if line.startswith("Sentiment:"):
            result["sentiment"] = line.replace("Sentiment:", "").strip()
        elif line.startswith("Summary:"):
            result["summary"] = line.replace("Summary:", "").strip()
        elif line.startswith("Key themes:"):
            result["key_themes"] = line.replace("Key themes:", "").strip()
    return result


if __name__ == "__main__":
    test = "This book is rated Five stars and priced at £9.99."
    output = analyze_review(test)
    print(output)
    print(parse_llm_output(output))