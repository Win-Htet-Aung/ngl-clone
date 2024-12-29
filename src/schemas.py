from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str


class UserCreateResponse(BaseModel):
    message: str
    username: str
