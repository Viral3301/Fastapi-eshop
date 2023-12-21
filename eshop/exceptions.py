from starlette.responses import HTMLResponse,RedirectResponse
from starlette.requests import Request
from fastapi import HTTPException





def not_found_error(request: Request, exc: HTTPException):
    return HTMLResponse(
        status_code=404,
        content=f"""
        <html>

        <head>
            <title>404 Not Found</title>
        </head>

        <body style="padding: 30px">
            <h1>404 Not Found</h1>
            <p>The resource could not be found.</p>
        </body>

        </html>
        """,
    )

def Unauthorized_redirect(request:Request,exc: HTTPException):
    return RedirectResponse('/login')
