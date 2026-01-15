from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import store

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/dashboard")
async def dashboard(request: Request):
    user = request.session.get("user")
    role = request.session.get("role")
    
    if not user:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

    my_reservations = []
    if role == "resident":
        my_reservations = store.get_reservations_for_user(user)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user": user,
        "role": role,
        "services": store.services_list,
        "reservations": my_reservations,
        "success_msg": request.query_params.get("success")
    })

@router.get("/reserve/{service_id}")
async def reserve_page(request: Request, service_id: int):
    if request.session.get("role") != "resident":
        return RedirectResponse(url="/dashboard")

    service = store.get_service_by_id(service_id)
    if not service:
        return RedirectResponse(url="/dashboard")

    return templates.TemplateResponse("reserve.html", {
        "request": request,
        "service": service,
        "error": request.query_params.get("error")
    })

@router.post("/reserve")
async def process_reservation(
    request: Request, 
    service_id: int = Form(...), 
    date: str = Form(...), 
    time: str = Form(...)
):
    user = request.session.get("user")
    if request.session.get("role") != "resident":
        return RedirectResponse(url="/login")

    service = store.get_service_by_id(service_id)
    
    success = await service.add_reservation(date, time, user)

    if success:
        return RedirectResponse(
            url="/dashboard?success=Reservation confirmed!", 
            status_code=status.HTTP_303_SEE_OTHER
        )
    else:
        return RedirectResponse(
            url=f"/reserve/{service_id}?error=Slot is full or unavailable.", 
            status_code=status.HTTP_303_SEE_OTHER
        )

@router.post("/cancel")
async def cancel_reservation(
    request: Request,
    service_id: int = Form(...),
    date: str = Form(...),
    time: str = Form(...)
):
    user = request.session.get("user")
    
    if request.session.get("role") != "resident":
        return RedirectResponse(url="/login")

    service = store.get_service_by_id(service_id)
    
    if service:
        await service.cancel_reservation(date, time, user)
        
    return RedirectResponse(
        url="/dashboard?success=Reservation cancelled successfully.", 
        status_code=status.HTTP_303_SEE_OTHER
    )