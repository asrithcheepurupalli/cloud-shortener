from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from datetime import datetime
from bson.objectid import ObjectId
from database import db
from models import new_url_entry, log_visit

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# GET: Homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# POST: Shorten a URL
@app.post("/shorten", response_class=HTMLResponse)
async def shorten_url(request: Request, long_url: str = Form(...)):
    entry = new_url_entry(long_url)
    db.urls.insert_one(entry)
    short_code = entry["short_code"]
host = request.url.scheme + "://" + request.url.hostname
short_url = f"{host}/{short_code}"

return templates.TemplateResponse("dashboard.html", {
    "request": request,
    "short_code": short_code,
    "short_url": short_url,
    "long_url": long_url,
    "timestamps": []

    })

# GET: Redirect by short code
@app.get("/{short_code}")
async def redirect_url(short_code: str):
    result = db.urls.find_one({"short_code": short_code})
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")

    db.urls.update_one(
        {"_id": result["_id"]},
        {"$push": {"visits": log_visit()}}
    )

    return RedirectResponse(result["long_url"])

# GET: Dashboard analytics
@app.get("/dashboard/{short_code}", response_class=HTMLResponse)
async def dashboard(request: Request, short_code: str):
    result = db.urls.find_one({"short_code": short_code})
    if not result:
        raise HTTPException(status_code=404, detail="URL not found")

    visits = result.get("visits", [])
    timestamps = [v["timestamp"].isoformat() for v in visits]

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "short_code": short_code,
        "long_url": result["long_url"],
        "timestamps": timestamps
    })