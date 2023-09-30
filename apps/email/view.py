"""
    Email View Module

    Description:
    - This module is responsible for email views.

"""

# Importing Python Packages
from datetime import datetime, timedelta
from jose import jwt

# Importing FastAPI Packages

# Importing Project Files
from core import core_configuration
from apps.base import BaseView
from apps.api_v1.user.model import UserTable
from apps.api_v1.user.schema import UserCreateSchema, UserUpdateSchema
from .configuration import email_configuration
from .response_message import email_response_message
from .schema import EmailBaseSchema, EmailDataSchema, EmailSchema
from .helper import generate_otp_code
from .send_email import send_email


# -----------------------------------------------------------------------------


# Email class
class EmailView(
    BaseView[
        UserTable,
        UserCreateSchema,
        UserUpdateSchema,
    ]
):
    """
    Email View Class

    Description:
    - This class is responsible for email views.

    """

    def __init__(
        self,
        model: UserTable,
    ):
        """
        Email View Class Initialization

        Description:
        - This method is responsible for initializing class.

        Parameter:
        - **model** (UserTable): User Database Model.

        """

        super().__init__(model=model)

    async def send_email_otp(self, record: EmailBaseSchema) -> dict:
        """
        Sends an email with OTP.

        Description:
        - This method is used to encode OTP code and send it to user via email.

        Parameters:
        Email details to be sent with following fields:
        - **subject** (STR): Subject of email. **(Required)**
        - **email_purpose** (STR): Purpose of email. **(Required)**
        - **user_name** (STR): Full name of user. **(Required)**
        - **email** (LIST): Email of user. **(Required)**

        Returns:
        - **details** (DICT): Details of email sent.

        """
        print("Calling send_email_otp method")

        # Generate OTP Code
        otp_code = await generate_otp_code()
        otp_expiry_time = datetime.utcnow() + timedelta(
            minutes=email_configuration.OTP_CODE_EXPIRY_MINUTES
        )

        # Encode OTP Code
        encoded_jwt = jwt.encode(
            claims={
                "email": record.email,
                "token": otp_code,
                "exp": otp_expiry_time.timestamp(),
            },
            key=core_configuration.OTP_CODE_SECRET_KEY,
            algorithm=core_configuration.ALGORITHM,
        )

        url = "".join(
            [
                core_configuration.CLIENT_BASE_URL,
                "/",
                record.email_purpose.replace(" ", "-").lower(),
                "/",
                encoded_jwt,
            ]
        )

        # Send Email
        email_response = await send_email(
            email=EmailSchema(
                email=[record.email],
                subject=record.subject,
                body=EmailDataSchema(
                    url=url,
                    otp_code=otp_code,
                    user_name=record.user_name,
                    email_purpose=record.email_purpose,
                    company_name=core_configuration.COMPANY_NAME,
                    base_url=core_configuration.CLIENT_BASE_URL,
                ),
            )
        )

        if email_response.get("success"):
            return {
                "success": True,
                "detail": email_response_message.EMAIL_SENT,
                "otp_code": otp_code,
            }

        return {
            "success": False,
            "detail": email_response_message.EMAIL_SENT_FAILED,
        }


email_view = EmailView(model=UserTable)
