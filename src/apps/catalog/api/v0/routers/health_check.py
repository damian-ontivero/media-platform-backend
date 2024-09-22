from fastapi import APIRouter
from fastapi import status

from apps.catalog.api.v0.controllers.health_check_controller import HealthCheckController
from apps.catalog.api.v0.dependecy_injection import container


router = APIRouter(tags=["Health check"])


@router.get("/health", response_model=str, status_code=status.HTTP_200_OK)
async def health_check():
    controller: HealthCheckController = container.find("HealthCheckController")

    return await controller.run(request=None)
