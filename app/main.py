from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.scraper.static import static_scrape
from app.scraper.js import js_scrape
from datetime import datetime, timezone

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/scrape")
async def scrape(payload: dict):
    url = payload.get("url")
    if not url or not url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL")

    errors = []
    try:
        result = await static_scrape(url)
        if len(result["sections"]) < 2:
            raise Exception("Static insufficient")
    except Exception as e:
        errors.append({"message": str(e), "phase": "static"})
        result = await js_scrape(url)

    result["errors"].extend(errors)
    return {"result": result}
