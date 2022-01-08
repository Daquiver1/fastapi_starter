from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .library.helpers import *


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory = "static"), name = "static")

@app.get("/", response_class = HTMLResponse)
async def home(request: Request):
	data = {
			"page": "Home page"
	}
	return templates.TemplateResponse("page.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
	data = openfile(page_name + ".md")
	return templates.TemplateResponse("page.html", {"request": request, "data": data})
