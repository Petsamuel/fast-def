# from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates/static", StaticFiles(directory="templates"), name="static")

api_url = "http://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word: str):
    try:
        response = requests.get(api_url + word)
        response.raise_for_status()  # Raise an exception if the response status is not 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle the request error gracefully
        return {"error": "Word not found or API request failed"}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    default_word = "welcome"  # Set a default word to fetch data on load
    data = get_definition(default_word)
    
    if data is None:
        raise HTTPException(status_code=404, detail="Word not found or API request failed")
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
    
@app.get("/word/{word}", response_class=HTMLResponse)
async def word(request: Request, word: str):
    if word == "":
        raise HTTPException(status_code=400, detail="Word is required")
    
    data = get_definition(word)
    
    if data is None:
        raise HTTPException(status_code=404, detail="Word not found or API request failed")
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.post("/word", response_class=HTMLResponse)
async def word(request: Request, word: str = Form(...)):
    data = get_definition(word)
    
    if data is None:
        raise HTTPException(status_code=404, detail="Word not found or API request failed")
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})



    

