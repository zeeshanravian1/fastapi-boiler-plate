"""
    Email Pydantic Validators

    Description:
    - This module contains validators for email pydantic schemas.

"""

# Importing Python packages
from random import randint

# Importing FastAPI packages

# Importing from project files


# -----------------------------------------------------------------------------


async def generate_otp_code() -> str:
    """
    Generates 6 digit OTP code.

    Description:
    - This method is used to generate a 6 digit OTP.

    Parameter:
    - **None**

    Return:
    - **otp_code** (STR): 6 digit OTP code.

    """
    print("Calling generate_otp_code method")

    return str(randint(100000, 999999))


def lowercase_email(email: str | list) -> str:
    """
    Lowercase Email

    Description:
    - This method is used to lowercase email passed to API.

    Parameter:
    - **email** (STR): Email to be lowercased. **(Required)**

    Return:
    - **email** (STR): Lowercased email.

    """
    print("Calling lowercase_email method")

    return email.lower()
