from schemas import UserRequest
from models import User
from sqlalchemy.orm import Session
from sqlalchemy import select


async def create_user(user_request: UserRequest, session: Session) -> User:
    user = User(username=user_request.username)
    n = 0
    while True:
        result = session.execute(select(User).where(User.username == user.username)).first()
        if result:
            n += 1
            user.username = f"{user_request.username}{n}"
        else:
            session.add(user)
            session.commit()
            return user

async def get_user(username: str, session: Session) -> User:
    result = session.execute(select(User).where(User.username == username)).first()
    return result
