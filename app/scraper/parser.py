def parse_sections(soup, url):
    sections = []
    for i, sec in enumerate(soup.find_all(["section", "main", "article"])):
        text = sec.get_text(" ", strip=True)
        if not text:
            continue

        sections.append({
            "id": f"section-{i}",
            "type": "section",
            "label": text.split()[:5],
            "sourceUrl": url,
            "content": {
                "headings": [h.text for h in sec.find_all(["h1", "h2", "h3"])],
                "text": text[:1000],
                "links": [
                    {"text": a.text, "href": a.get("href")}
                    for a in sec.find_all("a", href=True)
                ],
                "images": [],
                "lists": [],
                "tables": []
            },
            "rawHtml": str(sec)[:1000],
            "truncated": len(str(sec)) > 1000
        })
    return sections or [{
        "id": "fallback-0",
        "type": "unknown",
        "label": "Content",
        "sourceUrl": url,
        "content": {
            "headings": [],
            "text": soup.get_text(strip=True)[:1000],
            "links": [],
            "images": [],
            "lists": [],
            "tables": []
        },
        "rawHtml": "",
        "truncated": False
    }]
