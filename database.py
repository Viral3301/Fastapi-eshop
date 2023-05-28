from typing import AsyncGenerator
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Float,Date
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase,SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:223344@localhost/fastapi_eshop"

Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at",Date, default=datetime.now())
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified = Column("is_verified", Boolean, default=False, nullable=False)


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)



# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:223344@localhost/fastapi_eshop"