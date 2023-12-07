from httpx import AsyncClient
import os

async def test_create_category(ac: AsyncClient):
    response = await ac.post("/createcategory?name=test_accesory")

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_accessory(ac: AsyncClient):
    file = {'image': open(os.path.abspath("content_img/test_img.png"),"rb")}
    response = await ac.post("/create?title=Test_accessory&price=123&manufacturer=Test1&amount_in_stock=1&sale=false&category=1&rating=3",files=file)

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_create_vehicle(ac: AsyncClient):
    await ac.post("/createcategory?name=test_vehicle")
    file = {'image': open(os.path.abspath("content_img/test_img.png"),"rb")}
    response = await ac.post("createvehicle?title=Test_vehicle&price=123&manufacturer=Test2&seats=2&engine=123&engine_type=123&year=123&amount_in_stock=123&sale=true&category=2",files=file)

    assert response.status_code == 200
    assert response.json()["response"] == "good"

async def test_get_product_page(ac: AsyncClient):
    response = await ac.get("/product/1/1")

    assert response.status_code == 200

async def test_get_product_page_failed(ac: AsyncClient):
    response = await ac.get("/product/1234/1234")

    assert response.status_code == 404

async def test_search_by_name(ac: AsyncClient):
    response = await ac.post("/search_by_name?page_num=1", data={"name": 'te'})

    assert response.status_code == 200

async def test_search_by_code(ac: AsyncClient):
    response = await ac.post("/search_by_code", data={'code':111111})

    assert response.status_code == 200

async def test_search_by_manufacturer(ac: AsyncClient):
    response = await ac.post("/search_by_manufacturer?page_num=1", data={'manufacturer': 'test2'})

    assert response.status_code == 200