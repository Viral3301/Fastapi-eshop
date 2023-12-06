from eshop.models import Accessories
from conftest import client, async_test_session_maker
from main import app
import pytest
from httpx import AsyncClient

async def test_register():
    response = client.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
    })
    
    assert response.status_code == 201


# async def test_login():
#         data = "'grant_type=&username=string&password=string&scope=&client_id=&client_secret='"
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         response = client.post("/auth/jwt/login" ,data=data,headers=headers)

#         assert response.status_code == 204