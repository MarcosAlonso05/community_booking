from fastapi import FastAPI, Request
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse
from app.routers import auth, services

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="super_secret_key_123")

app.include_router(auth.router)
app.include_router(services.router)

@app.get("/")
async def root(request: Request):
    if request.session.get("user"):
        return RedirectResponse(url="/dashboard")
    return RedirectResponse(url="/login")