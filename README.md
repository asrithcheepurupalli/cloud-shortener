# Cloud URL Shortener with Analytics

A simple cloud-based URL shortening service built using FastAPI, MongoDB, and Chart.js for visual analytics.

## Features

- Shorten any valid URL to a custom code.
- Track visits and visualize analytics per short link.
- Dashboard built using HTML + Chart.js.
- FastAPI + MongoDB integration.
- Responsive UI with minimal dependencies.

## Folder Structure

```
cloud-shortener/
├── main.py            # FastAPI app entrypoint
├── database.py        # MongoDB connection
├── models.py          # Data handling utilities
├── templates/         # HTML templates (dashboard)
│   └── dashboard.html
├── static/
│   └── chart.css      # Styling and chart visuals
├── .env               # Secrets (MONGO_URI, DB_NAME)
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Create a `.env` file in the root:

```
MONGO_URI=your_mongodb_connection_uri
DB_NAME=shortener
```

3. Run the app:

```
uvicorn main:app --reload
```

Open your browser at http://127.0.0.1:8000

## Deployment

Deploy on [Render](https://render.com), [Railway](https://railway.app), or [Fly.io](https://fly.io) using the FastAPI-compatible build.

## Dependencies

- fastapi
- uvicorn
- jinja2
- pymongo
- python-dotenv

## Author

Lok Sai Asrith Cheepurupalli  
https://asrithcheepurupalli.codes
