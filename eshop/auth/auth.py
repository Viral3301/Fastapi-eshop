from typing import Any
from fastapi.responses import RedirectResponse
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

class CookieRedirectTransport(CookieTransport):
    async def get_login_response(self, token: str) -> Any:
        response = RedirectResponse("https://http://127.0.0.1:8000/profile", 302)
        self._set_login_cookie(response, token)
        return response


cookie_transport = CookieRedirectTransport(cookie_max_age=3600)


SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)