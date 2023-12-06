from httpx import AsyncClient
import os

async def test_create_category(ac: AsyncClient):
    response = await ac.post("/createcategory?name=test_accesory")

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_accessory(ac: AsyncClient):
    file = {'image': open(os.path.abspath("content_img/test_img.png"),"rb")}
    response = await ac.post("/create?title=test&price=123&manufacturer=test&amount_in_stock=1&sale=false&category=1&rating=3",files=file)

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_vehicle(ac: AsyncClient):
    await ac.post("/createcategory?name=test_vehicle")
    file = {'image': open(os.path.abspath("content_img/test_img.png"),"rb")}
    response = await ac.post("/create?title=test&price=123&manufacturer=test&amount_in_stock=1&sale=false&category=1&rating=3",files=file)

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_get_product_page(ac: AsyncClient):
    response = await ac.get("/product/1/1")

    assert response.status_code == 200