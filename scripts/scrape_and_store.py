# scripts/scrape_and_store.py
from backend.mongo.models import db
from backend.scraper.scraper import scrape_website

URLS_TO_SCRAPE = [
    "https://www.zconsolutions.com/",
    "https://www.zconsolutions.com/careers/",
    "https://www.zconsolutions.com/team/",
    "https://www.zconsolutions.com/success_stories/"
]

def store_data(doc):
    # Flatten the content array into one string
    if isinstance(doc.get("content"), list):
        doc["content"] = " ".join([c.strip() for c in doc["content"] if c.strip() != ""])
    db.pages.insert_one(doc)
    print(f"Stored data from {doc['url']}")

def main():
    for url in URLS_TO_SCRAPE:
        data = scrape_website(url)
        store_data(data)

if __name__ == "__main__":
    main()



# import asyncio
# from backend.mongo.models import db
# from backend.scraper.scraper import scrape_website

# URLS_TO_SCRAPE = [
#  "https://www.zconsolutions.com/customer-enagagement/agile-methodology/"
# ]

# def store_data(doc):
#     db.pages.insert_one(doc)
#     print(f"Stored data from {doc['url']}")

# def main():
#     for url in URLS_TO_SCRAPE:
#         data = scrape_website(url)
#         store_data(data)

# if __name__ == "__main__":
#     main()
