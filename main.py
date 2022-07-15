from urllib import request
import requests
from fastapi import FastAPI, Response
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

# API endpoint
# Run 'uvicorn main:app --reload' and go to url to get JSON information
@app.get("/")
async def jobs_list():
    return scraper.find_jobs()