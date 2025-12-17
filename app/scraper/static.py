import httpx
from bs4 import BeautifulSoup
from app.scraper.parser import parse_sections
from datetime import datetime, timezone

async def static_scrape(url):
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(url)
        soup = BeautifulSoup(r.text, "lxml")

    return {
        "url": url,
        "scrapedAt": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "title": soup.title.text if soup.title else "",
            "description": "",
            "language": soup.html.get("lang", "en") if soup.html else "en",
            "canonical": None
        },
        "sections": parse_sections(soup, url),
        "interactions": {
            "clicks": [],
            "scrolls": 0,
            "pages": [url]
        },
        "errors": []
    }
