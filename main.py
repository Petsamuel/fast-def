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
    response = requests.get(api_url + word)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Word not found or API request failed"}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.get("/word/{word}", response_class=HTMLResponse)
async def word(request: Request, word: str):
    if word == "":
        return templates.TemplateResponse("error.html", {"request": request, "error": "Word is required"})
    else:
        data = get_definition(word)
        return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.post("/word", response_class=HTMLResponse)
async def word(request: Request, word: str = Form(...)):
    data = get_definition(word)
    return templates.TemplateResponse("index.html", {"request": request, "data": data})



    

