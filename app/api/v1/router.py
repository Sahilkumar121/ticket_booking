from fastapi import APIRouter

from .endpoints import user

route = APIRouter(prefix="/v1")

route.include_router(user.route)
