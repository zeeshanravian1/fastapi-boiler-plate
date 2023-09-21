"""
    User Configuration Module

    Description:
    - This module is responsible for user configuration.

"""

# Importing Python Packages

# Importing FastAPI Packages

# Importing Project Files


# -----------------------------------------------------------------------------


class UserConfiguration:
    """
    User Settings Class

    Description:
    - This class is used to define User configurations.

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
    USER_COLUMN_USERNAME: str = "username"
    USER_COLUMN_EMAIL: str = "email"


user_configuration = UserConfiguration()
