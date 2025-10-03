
import re
from fastapi import FastAPI
from backend.mongo.models import db
from pymongo import TEXT

app = FastAPI()

# Ensure text index exists
db.pages.create_index([("content", TEXT)])

@app.get("/query")
def query_data(q: str):
    """
    Search MongoDB content using full-text search.
    Returns only paragraphs that contain at least one keyword from the query.
    """
    print(f"\n🔍 Received query: {q}")   # log query

    results = db.pages.find(
        {"$text": {"$search": q}},
        {"score": {"$meta": "textScore"}, "content": 1, "url": 1}
    ).sort([("score", {"$meta": "textScore"})])
 
    output = []
    for r in results:
        # Split content into paragraphs by dot or newline
        paragraphs = re.split(r'\. |\n', r["content"])
        # Filter paragraphs containing at least one query word
        matched = [p.strip() for p in paragraphs if any(word.lower() in p.lower() for word in q.split())]
        if matched:
            # Take first 3 matches as snippet
            snippet = " ".join(matched[:3])
            # Truncate snippet to 1000 chars to avoid huge messages
            snippet = snippet[:1000]
            output.append({
                "url": r["url"],
                "snippet": snippet
            })
    
    print(f"✅ Response: {output}\n")   # log response
    return output










# # backend/main.py
# import json
# import re
# from fastapi import FastAPI

# app = FastAPI()

# # Load JSON once at startup
# with open("test.json", "r", encoding="utf-8") as f:
#     DATA = json.load(f)

# @app.get("/query")
# def query_data(q: str):
#     """
#     Search through test.json and return snippets matching the query.
#     """
#     results = []
#     search_results = DATA.get("searchResponse", {}).get("results", [])

#     for r in search_results:
#         doc = r.get("document", {}).get("derivedStructData", {})
#         snippets = doc.get("snippets", [])
#         snippet_texts = [s.get("snippet", "") for s in snippets]

#         # Check if any snippet contains any word from query
#         matched = [s for s in snippet_texts if any(word.lower() in s.lower() for word in q.split())]
#         if matched:
#             snippet = " ".join(matched)[:4000]  # Limit to 1000 chars
#             results.append({
#                 "url": doc.get("link", ""),
#                 "snippet": snippet
#             })

#     return results


