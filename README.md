# 📌 Telegram Bot (Web Scraper + Q&A)

This project is a **Telegram chatbot** that scrapes content from a website, stores it in MongoDB, and allows users to query the data via natural questions.

---

## 🚀 How to Run

You’ll need to open **3 terminals** and run the following commands:

### 1️⃣ Scrape and Store Website Data
```bash
python -m scripts.scrape_and_store
```
> Scrapes content from the configured website/URL and stores it in the MongoDB database.

---

### 2️⃣ Start the Backend API
```bash
uvicorn backend.main:app --reload
```
> Runs the FastAPI backend which handles search queries from the bot.

---

### 3️⃣ Run the Telegram Bot
```bash
python bot/bot.py
```
> Starts the Telegram bot that interacts with users and fetches responses from the backend.

---

## ✅ Flow
1. **Scraper** → Extracts website content and saves to DB.  
2. **Backend** → Exposes a search API over the stored data.  
3. **Telegram Bot** → Answers user queries by calling the backend.  

---

## 🛠️ Requirements
- Python 3.10+  
- MongoDB running locally or in the cloud  
- Dependencies from `requirements.txt`  

---

## 📌 Example
- User: `What is Agile?`  
- Bot: Returns the relevant snippet from the scraped website.  
