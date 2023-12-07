import uuid
from typing import Optional
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, UUIDIDMixin,IntegerIDMixin
from starlette.templating import Jinja2Templates
from database import User, get_user_db

SECRET = "SECRET"

templates = Jinja2Templates(directory="templates")

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


    async def on_after_register(self, user: User, request: Optional[Request] = None,):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)