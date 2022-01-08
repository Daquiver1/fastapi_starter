from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory = "templates")

router = APIRouter()

@router.get("/unsplash", response_class = HTMLResponse)
async def unsplash_home(request: Request):
	return templates.TemplateResponse("unsplash.html", {"request": request})