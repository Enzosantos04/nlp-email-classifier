from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.service_ai import classify


app = FastAPI()

template = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# esse endpoint renderiza a pagina inicial html
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


# esse endpoint processa o formulario enviado na pagina inicial e retorna a classificacao do email.
@app.post("/classify", response_class=HTMLResponse)
def classify_email(request: Request, email_content: str = Form(...)):
    result = classify(email_content)
    return template.TemplateResponse("index.html", {"request": request, "category": result["category"], "classification": result["classification"]})
