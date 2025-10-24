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
    booths = session.exec(select(Booth.id,Booth.name,School.name,Booth.img).join(School).order_by(School.name)).all()
    print(booths)
    return templates.TemplateResponse("booth.html", {"request": request, "booths": booths})

@router.get("/booth/{booth_id}")
async def boothdetail(request:Request, booth_id:int ,session:SessionDep):
    boothinfo = session.exec(select(Booth).where(Booth.id == booth_id)).all()
    print(boothinfo)
    return templates.TemplateResponse("boothdetail.html", {"request": request, "booth": boothinfo})


@router.get("/school")
async def schoollist(request:Request, session:SessionDep):
    schools = session.exec(select(School.id,School.name,School.img)).all()
    print(schools)
    return templates.TemplateResponse("school.html", {"request": request, "schools": schools})

@router.get("/school/{school_id}")
async def schooldetail(request:Request, school_id:int, session:SessionDep):
    schoolinfo = session.exec(select(School).where(School.id == school_id)).all()
    return templates.TemplateResponse("schooldetail.html", {"request": request, "school": schoolinfo})

@router.get("/event")
async def eventlist(request:Request, session:SessionDep):
    events = session.exec(select(Event.id,Event.name,School.name,Event.img,Event.time_start,Event.time_end).join(School)).all()
    return templates.TemplateResponse("event.html", {"request": request, "events": events})
    
@router.get("/event/{event_id}")
async def eventdetail(request:Request, event_id:int ,session:SessionDep):
    eventinfo = session.exec(select(Event).where(Event.id == event_id)).all()
    return templates.TemplateResponse("eventdetail.html", {"request": request, "event": eventinfo})