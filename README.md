# 📧 Gmail Automation System (Playwright + Python + Django)

## 🚀 Project Overview

The Gmail Automation System is a Python-based automation project that:

-   Logs into Gmail using Playwright\
-   Scrapes unread emails from Inbox (and optionally Spam)\
-   Stores email data in a SQLite database\
-   Exports data into CSV and Excel formats\
-   Optionally displays data in a Django web dashboard

This project demonstrates real-world automation, data scraping, and
backend integration.

------------------------------------------------------------------------

## 🎯 Features

-   Automated Gmail scraping\
-   Secure login session using storage_state.json\
-   SQLite database integration\
-   Export emails to CSV (emails.csv)\
-   Export emails to Excel (emails.xlsx)\
-   Clean modular code structure\
-   Optional Django dashboard

------------------------------------------------------------------------

## 🗂️ Project Structure

gmail_playwright_system/

├── main.py\
├── login_session.py\
├── gmail_scraper.py\
├── database.py\
├── export_csv.py\
├── export_excel.py\
├── emails.db\
├── storage_state.json\
└── django_dashboard/

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python 3.10 or higher\
-   Playwright\
-   Pandas\
-   OpenPyXL\
-   Django (optional)

------------------------------------------------------------------------

## 📦 Installation

### 1. Clone the Repository

git clone `<your-repo-link>`{=html}\
cd gmail_playwright_system

------------------------------------------------------------------------

### 2. Create Virtual Environment

python -m venv .venv\
.venv`\Scripts`{=tex}`\activate  `{=tex}

------------------------------------------------------------------------

### 3. Install Dependencies

pip install playwright pandas openpyxl django\
playwright install

------------------------------------------------------------------------

## 🔐 Step 1: Login to Gmail (IMPORTANT)

Run:

python login_session.py

-   A browser will open\
-   Login to Gmail manually\
-   Press ENTER in terminal

This creates: storage_state.json

------------------------------------------------------------------------

## 📥 Step 2: Run the System

python main.py

------------------------------------------------------------------------

## ⚙️ What Happens Internally

1.  Database is created (emails.db)\
2.  Gmail opens using saved session\
3.  Emails are scraped\
4.  Data is stored in SQLite\
5.  Data is exported to CSV & Excel

------------------------------------------------------------------------

## 📊 Output Files

-   emails.db\
-   emails.csv\
-   emails.xlsx

------------------------------------------------------------------------

## 🌐 (Optional) Run Django Dashboard

cd django_dashboard\
python manage.py runserver

Open in browser:\
http://127.0.0.1:8000

------------------------------------------------------------------------

## ⚠️ Common Issues & Fixes

Gmail login blocked → Use real Chrome or persistent session

storage_state.json not found → Run python login_session.py

Import errors → Check function names: - save_email()\
- export_to_csv()\
- export_to_excel()

Playwright not working → Run playwright install

Indentation errors → Use 4 spaces

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Auto scheduler\
-   Advanced Django dashboard\
-   Search & filters\
-   REST API\
-   Docker support

------------------------------------------------------------------------

## 👨‍💻 Author

Bishwaprotap Ray\
CSE Student \| Aspiring Machine Learning Engineer\
GitHub: https://github.com/Bishwaprotapi

------------------------------------------------------------------------

## ⭐ Conclusion

This project demonstrates:

-   Web automation using Playwright\
-   Data scraping and processing\
-   Database management\
-   File export systems\
-   Full-stack extension with Django

------------------------------------------------------------------------

🔥 A complete real-world automation project for learning and portfolio
use.
