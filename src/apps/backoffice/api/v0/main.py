import contextlib

from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse

from apps.backoffice.api.v0.dependecy_injection import container
from apps.backoffice.api.v0.exception import EXCEPTION_TO_HTTP_STATUS_CODE
from apps.backoffice.api.v0.routers.health_check import router as health_check_router
from apps.backoffice.api.v0.routers.media import router as media_router
from apps.backoffice.api.v0.routers.movies import router as movies_router
from apps.backoffice.api.v0.routers.series import router as series_router
from contexts.shared.domain.event_bus.event_bus import EventBus


@contextlib.asynccontextmanager
async def configure_event_bus(app: FastAPI):
    event_bus: EventBus = container.find("EventBus")
    await event_bus.add_subscribers()
    yield


app = FastAPI(
    title="Media Platform - Backoffice - API",
    description="This is the API documentation for the Media Platform Backoffice API.",
    version="0.1.0",
    root_path="/backoffice/api/v0",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
    lifespan=configure_event_bus,
)

# CORS
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"]
)

# Routers
app.include_router(router=health_check_router)
app.include_router(router=media_router)
app.include_router(router=movies_router)
app.include_router(router=series_router)


# Setups the exception handler
@app.exception_handler(Exception)
def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content={"message": str(exception)}, status_code=EXCEPTION_TO_HTTP_STATUS_CODE.get(exception.__class__, 500)
    )


@app.get("/swagger", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(title=app.title, openapi_url=app.root_path + app.openapi_url)


@app.get("/documentation", include_in_schema=False)
def overridden_redoc():
    return get_redoc_html(title=app.title, openapi_url=app.root_path + app.openapi_url)
