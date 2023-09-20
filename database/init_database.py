"""
    Insert initial data in database.

    Description:
    - This module is responsible for inserting initial data in database.

"""

# Importing Python Packages
from passlib.hash import pbkdf2_sha256
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.engine.result import ChunkedIteratorResult
from sqlalchemy.sql.selectable import Select

# Importing FastAPI Packages

# Importing Project Files
from apps.api_v1.role.model import RoleTable
from core import core_configuration


# -----------------------------------------------------------------------------


# Insert database data
async def insert_db_data(db_session: async_sessionmaker[AsyncSession]) -> None:
    """
    Insert Database Data

    Description:
    - This function is used to insert initial data in database.

    Parameter:
    - **db_session** (async_sessionmaker[AsyncSession]): Database session.

    Return:
    - **None**

    """
    print("Calling insert_db_data method")

    try:
        async with db_session() as session:
            async with session.begin():
                # Insert Roles in database
                session.add_all(
                    instances=[
                        RoleTable(
                            role_name=core_configuration.SUPERUSER_ROLE,
                            role_description=core_configuration.SUPERUSER_ROLE_DESCRIPTION,
                        ),
                        RoleTable(
                            role_name="admin",
                            role_description="Admin Role Description",
                        ),
                        RoleTable(
                            role_name="manager",
                            role_description="Manager Role Description",
                        ),
                        RoleTable(
                            role_name="user",
                            role_description="User Role Description",
                        ),
                    ]
                )

                await session.commit()

    except Exception:
        pass
