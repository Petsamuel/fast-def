from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates/static", StaticFiles(directory="templates"), name="static")

URL = os.getenv("ApiUrl")

def get_definition(word: str):
    try:
        response = requests.get(URL + word.lower())  # Convert word to lowercase
        response.raise_for_status()  # Raise an exception if the response status is not 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle the request error gracefully
        return None

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    default_word = "example"  # Set a default word to fetch data on load
    data = get_definition(default_word)
    
    if data is None:
        error_message = "Word not found or API request failed"
        return templates.TemplateResponse("index.html", {"request": request, "error_message": error_message})
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
    
@app.get("/word/{word}", response_class=HTMLResponse)
async def word(request: Request, word: str):
    if word == "":
        raise HTTPException(status_code=400, detail="Word is required")
    
    data = get_definition(word)
    
    if data is None:
        error_message = "Word not found or API request failed"
        return templates.TemplateResponse("index.html", {"request": request, "error_message": error_message})
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.post("/word", response_class=HTMLResponse)
async def word(request: Request, word: str = Form(...)):
    data = get_definition(word)
    
    if data is None:
        error_message = "Word not found or API request failed"
        return templates.TemplateResponse("index.html", {"request": request, "error_message": error_message})
    
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

# Catch-all route to handle invalid endpoints
@app.get("/{path:path}", response_class=RedirectResponse)
async def catch_all(path: str):
    return RedirectResponse(url="/", status_code=302)