🌐 Web Content Extractor

A FastAPI-based web application that extracts static and JavaScript-rendered website content and converts it into structured JSON.
This project supports dynamic websites, pagination, and section-based extraction, making it useful for AI pipelines, data analysis, and automation.

📸 Project Preview

Home Page
<img width="1366" height="688" alt="image" src="https://github.com/user-attachments/assets/8e4269b8-7a0b-462f-a3a4-1cf8bd9b5b64" />

Scraped Output
<img width="1366" height="728" alt="image" src="https://github.com/user-attachments/assets/b45bd433-5a20-4b71-94d1-4b824be0709e" />

Structured JSON Output 
<img width="1366" height="728" alt="image" src="https://github.com/user-attachments/assets/98b80b34-b321-4e73-afa6-60b49b413f8e" />


🚀 Features
1. Extracts content from static & JS-heavy websites
2. Uses Playwright for JavaScript rendering
3. Converts website content into structured JSON
4. Section-based content extraction
5. Clean and responsive UI
6. Download extracted data as JSON
7. Visual success indicator after scraping

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: FastAPI (Python)
Scraping: BeautifulSoup, Playwright
Server: Uvicorn

📂 Project Structure
web-content-extractor/
│
├── app/
│   ├── main.py
│   ├── scraper/
│   │   ├── static.py
│   │   ├── js.py
│   │   └── parser.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── run.sh
├── README.md


▶️ How to Run the Project in VS Code
1. pip install
2. pip install -r requirements.txt
3. uvicorn app.main:app --reload --port 8000
4. python -m uvicorn app.main:app --reload
5. Open in Browser
http://127.0.0.1:8000

## Run Instructions
chmod +x run.sh
./run.sh

Visit http://localhost:8000

## Limitations
- Same-origin only
- Basic interaction heuristics

🧪 How the Project Works
1. User enters a website URL in the UI
2. Frontend sends request to /scrape API
3. Backend tries static scraping first
4. If content is dynamic → Playwright fallback
5. Page content is parsed into sections
6. Structured JSON is returned
7. UI displays sections and allows JSON download

## Tested URLs
1. https://www.coursera.org/
2. https://vercel.com
3. https://www.figma.com/

🎯 Use Cases
AI / LLM data ingestion (RAG)
Web content analysis
Automation pipelines
Website content monitoring
Search indexing
