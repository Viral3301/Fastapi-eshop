from httpx import AsyncClient
import os
from eshop.models import ProductAttributes

async def test_create_category(ac: AsyncClient):
    response = await ac.post("create/category?name=test_category")

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_product(ac: AsyncClient):
    file = {'image': open(os.path.abspath("content_img/test_img.png"),"rb")}
    response = await ac.post("create/accessory?title=Test_product&category=1&price=123&product_code=111111&sale=false",files=file)

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_attribute(ac: AsyncClient):
    response = await ac.post("create/attribute?title=manufacturer")

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_value(ac: AsyncClient):
    response = await ac.post("create/value?product_id=1&attribute_id=1&value=Китай")

    assert response.status_code == 200
    assert response.json()["response"] == "good"


async def test_search_by_name(ac: AsyncClient):
    response = await ac.post("search/search_by_name?page_num=1", data={"name": 'te'})

    assert response.status_code == 200

async def test_search_by_code(ac: AsyncClient):
    response = await ac.post("search/search_by_code", data={'code':111111})

    assert response.status_code == 200

async def test_search_by_manufacturer(ac: AsyncClient):
    response = await ac.post("search/search_by_manufacturer?page_num=1", data={'manufacturer': 'Китай'})

    assert response.status_code == 200

