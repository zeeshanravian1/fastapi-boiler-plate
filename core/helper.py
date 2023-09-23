"""
    Core Helper Module

    Description:
    - This module contains all helper functions used by core module.
"""

# Importing Python Packages
from pydantic import PostgresDsn

# Importing FastAPI Packages
from fastapi.routing import APIRoute

# Importing Project Files


# -----------------------------------------------------------------------------


# Unique ID Generator for Routes
def custom_generate_unique_id(route: APIRoute) -> str:
    """
    Custom Generate Unique ID

    Description:
    - This function is used to return a custom unique id for routes.

    Parameter:
    - **route** (APIRoute): Route object. **(Required)**

    Return:
    - **id** (STR): Custom unique id.

    """

    return f"{route.tags[0]}-{route.name}"


# Assembly DB Connection
def assemble_db_connection(url: str | None, values: dict[str, any]) -> any:
    """
    Assemble DB Connection

    Description:
    - This method is used to assemble database connection.

    Parameter:
    - **url** (STR): Database url. **(Optional)**
    - **values** (JSON): Values of database configurations. **(Required)**

    Return:
    - **database_url** (PostgresDsn): Database url.

    """

    if isinstance(url, str):
        return url

    return PostgresDsn.build(
        scheme=values.get("DATABASE"),
        host=values.get("DB_HOST"),
        port=values.get("DB_PORT"),
        username=values.get("DB_USER"),
        password=values.get("DB_PASSWORD"),
        path=f"{values.get('DB_NAME') or ''}",
    )
