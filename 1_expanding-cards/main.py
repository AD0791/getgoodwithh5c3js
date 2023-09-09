from fastapi import FastAPI, status, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from uvicorn import run


app = FastAPI(title="Expanding Cards")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class Home(BaseModel):
    welcome: str


@app.get("/", response_model=Home, status_code=status.HTTP_200_OK, tags=["expanding api"])
async def home():
    return Home(welcome="To the Expanding cards application")


@app.get('/expanding', response_class=HTMLResponse, tags=['expanding web app'])
async def expanding(req: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"request": req},
        status_code=status.HTTP_200_OK
    )

if __name__ == "__main__":
    run(
        "main:app",
        reload=True,
        port=8000
    )
