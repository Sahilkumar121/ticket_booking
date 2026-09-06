from fastapi import APIRouter, status

route = APIRouter(prefix="/user", tags=["USER"])


@route.get("/me", status_code=status.HTTP_200_OK)
def user_home():
    return {"success": True, "message": "This is user home page"}
