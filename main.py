from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/templates/static", StaticFiles(directory="templates"), name="static")
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class UnicodeConversionRequest(BaseModel):
    unicode_text: str
    

@app.post("/convert/", response_class=JSONResponse)
def convert_unicode(request: UnicodeConversionRequest):
    if not request.unicode_text:
        return JSONResponse(content={"error": "The `unicode_text` attribute is required."}, status_code=400)

    utf8_bytes = request.unicode_text.encode("utf-8")
    utf8_string = utf8_bytes.decode("utf-8")
    
    # Return the result as JSON
    return JSONResponse(content={"utf8_string": utf8_string})
