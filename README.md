<p align="center">
      <img src="https://i.ibb.co/g9ZvxZq/Group-159-2.png" width="140">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python Version">
   <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
</p>

## About

Drive moto is an online store with a catalog, a shopping cart, caching via redis, pagination , a user’s personal account, an administration panel, JWT authorization and the ability to search for a product by product code, name, country of manufacturer.

## Tech Stack

### Backend
* Python 3.11
* FastAPI
* Pydantic
* Alembic
* FastAPI-Users
* Aioredis
  
### Frontend
* HTML
* CSS
* JS (jQuery, Fetch API)

### Containerization
*  Docker
*  Docker-compose

### Web Servers
* gunicorn
* uvicorn

### Databases
* PostgreSQL
* Redis
  
## Installation
Install [Docker](https://www.docker.com/)

Set your own parameters in ```.env``` and ```.env-prod``` files

```docker build . -t fastapi_app```

```docker-compose build```

```docker-compose up```

Which will create FastAPI,Redis and PostgreSQL containers

Note: There is ```dump.sql``` file that contains example database and data,it can be changed or deleted if you dont need it.


## License
MIT
