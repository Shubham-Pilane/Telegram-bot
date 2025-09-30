import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all paragraphs as an example
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    return {"url": url, "content": paragraphs}
