from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query,Request
from sqlmodel import select, Session
from fastapi.templating import Jinja2Templates

from models import School,Booth,Event
from database import get_session


SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()


# Jinja2テンプレートの設定
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def main(request:Request, session:SessionDep):
    return templates.TemplateResponse("index.html", {"request": request}) 

@router.get("/booth")
async def boothlist(request:Request, session:SessionDep):
    users = session.exec()
    return templates.TemplateResponse("booth.html", {"request": request})

@router.get("/school")
async def schoollist(request:Request, session:SessionDep):
    return templates.TemplateResponse("school.html", {"request": request})

@router.get("/event")
async def eventlist(request:Request, session:SessionDep):
    return templates.TemplateResponse("event.html", {"request": request})
    