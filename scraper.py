# Web Scraper for News Headlines
# Uses requests + BeautifulSoup to fetch and save headlines

import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"   # You can change to any news site
OUTPUT_FILE = "headlines.txt"

def fetch_headlines():
    try:
        # Send a GET request with headers (to avoid blocking)
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(URL, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print("Failed to fetch webpage, status code:", response.status_code)
            return []

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all h2 tags (most headlines are in h2 on news sites)
        headlines = [h2.text.strip() for h2 in soup.find_all("h2")]

        return headlines

    except Exception as e:
        print("Error:", e)
        return []

def save_headlines(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"Saved {len(headlines)} headlines to {OUTPUT_FILE}")

def main():
    print("Fetching headlines from:", URL)
    headlines = fetch_headlines()

    if headlines:
        print("\nTop Headlines:\n")
        for i, h in enumerate(headlines[:10], start=1):  # Show first 10
            print(f"{i}. {h}")

        save_headlines(headlines)
    else:
        print("No headlines found!")

if __name__ == "__main__":
    main()
