from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from schemas import UserRequest, UserCreateResponse
from services import users as user_service
from database import get_session


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserCreateResponse)
async def create_user(user: UserRequest, session = Depends(get_session)):
    created_user = await user_service.create_user(user, session)
    content = UserCreateResponse(
        message="user created",
        username=created_user.username,
    )    
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=content.model_dump(),
    )

@router.get("/{username}")
async def get_user(username: str, session = Depends(get_session)):
    user = await user_service.get_user(username, session)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "user not found"},
        )
    user = user[0]
    content = {
        "message": "user found",
        "user": {
            "username": user.username,
            "id": user.id,
            "links": [],
        }
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=content,
    )
