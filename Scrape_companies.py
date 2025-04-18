from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def google_search(query, num_results=5):
    print(f"Searching Google for: {query}")
    return list(search(query, num_results=num_results))

def get_page_info(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else "No Title"
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
        return {
            "url": url,
            "title": title,
            "emails": list(emails)
        }
    except Exception as e:
        return {"url": url, "error": str(e)}

query = "Tecmantras software development company"
results = google_search(query, num_results=5)

scraped_data = []
for link in results:
    info = get_page_info(link)
    scraped_data.append(info)

for data in scraped_data:
    print("\n---")
    for k, v in data.items():
        print(f"{k.capitalize()}: {v}")
        
df = pd.DataFrame(scraped_data)
output_file = "tecmantras_scraped_data.xlsx"
df.to_excel(output_file, index=False)

print(f"\nData saved to {output_file}")
