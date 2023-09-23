"""
    User Configuration Module

    Description:
    - This module is responsible for user configuration.

"""

# Importing Python Packages
from enum import Enum

# Importing FastAPI Packages

# Importing Project Files


# -----------------------------------------------------------------------------


class UserConfiguration:
    """
    User Settings Class

    Description:
    - This class is used to define user configurations.

    """

    FIRST_NAME: str = "John"
    LAST_NAME: str = "Doe"
    CONTACT: str = "(02) 123-4567"
    USERNAME: str = "johndoe"
    EMAIL: str = "johndoe@email.com"
    PASSWORD: str = "12345@Aa"
    ADDRESS: str = "123 St, Lahore, Pakistan"
    CITY: str = "Lahore"
    STATE: str = "Punjab"
    COUNTRY: str = "Pakistan"
    POSTAL_CODE: str = "54000"
    ROLE_ID: int = 1
    IS_ACTIVE: bool = True
    USER_COLUMN_USERNAME: str = "username"
    USER_COLUMN_EMAIL: str = "email"


class UserTokenStatus(str, Enum):
    """
    User Token Status Enum

    Description:
    - This enum is used to define user token status.

    """

    LOGIN: str = "login"
    LOGOUT: str = "logout"


user_configuration = UserConfiguration()
