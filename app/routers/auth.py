from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import store

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login")
async def login_page(request: Request):
    error_message = request.query_params.get("error")
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": error_message
    })

@router.post("/login")
async def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    user = store.get_user_by_username(username)

    if user and user.password == password:
        request.session["user"] = user.username
        request.session["role"] = "resident"
        return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    
    return templates.TemplateResponse("login.html", {
        "request": request, 
        "error": "Invalid credentials."
    })

@router.post("/login/guest")
async def guest_login(request: Request):
    request.session["user"] = "Guest Visitor"
    request.session["role"] = "guest"
    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)