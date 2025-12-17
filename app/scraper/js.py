from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from app.scraper.parser import parse_sections
from datetime import datetime, timezone

async def js_scrape(url):
    pages = []
    sections = []
    scrolls = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")

        for depth in range(3):  # depth ≥ 3
            await page.mouse.wheel(0, 3000)
            await page.wait_for_timeout(1500)
            scrolls += 1

            html = await page.content()
            soup = BeautifulSoup(html, "lxml")

            sections.extend(parse_sections(soup, page.url))
            pages.append(page.url)

            # try clicking "More / Next"
            next_link = await page.query_selector("a:has-text('More'), a:has-text('Next')")
            if next_link:
                await next_link.click()
                await page.wait_for_timeout(1500)
            else:
                break

        await browser.close()

    return {
        "url": url,
        "scrapedAt": datetime.now(timezone.utc).isoformat(),
        "meta": {
            "title": "",
            "description": "",
            "language": "en",
            "canonical": None
        },
        "sections": sections or [],
        "interactions": {
            "clicks": ["next / more"],
            "scrolls": scrolls,
            "pages": list(set(pages))
        },
        "errors": []
    }
