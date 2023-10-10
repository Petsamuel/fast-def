from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Request, Form, HTTPException,File, UploadFile
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from docx2pdf import convert


templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/templates/static", StaticFiles(directory="templates"), name="static")


class UnicodeConversionRequest(BaseModel):
    emoji_text: str
    
    
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_word_to_pdf(file: UploadFile):
    # Check if the uploaded file has a valid .docx extension
    if file.filename.endswith('.docx'):
        # Save the uploaded file to a temporary location
        with open(file.filename, "wb") as f:
            f.write(file.file.read())

        # Convert the Word document to PDF
        convert(file.filename)

        # Return the PDF file
        pdf_filename = file.filename.replace('.docx', '.pdf')
        return {"message": "Conversion successful", "pdf_filename": pdf_filename}
    else:
        return {"error": "Invalid file format. Please upload a .docx file."}


