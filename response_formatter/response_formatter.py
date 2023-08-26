## The purpose of this script is to format bot answers entered into *input_data.jsonl* so they can be pass the test described in *dataformat_checker.py*

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def convert_to_explicit_format(text: str) -> str:
    """
    Adjusts the text to:
    - Escape all double quotes.
    - Escape backslashes.
    """
    # Escape backslashes first to ensure they are treated as literals
    text = text.replace('\\', '\\\\')
    
    # Escape all double quotes
    text = text.replace('"', '\\"')
        
    return text


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/process/")
def process_text(request: Request, text: str = Form(...)):
    result = convert_to_explicit_format(text)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

# start command local: uvicorn response_formatter:app --reload --port 8888
