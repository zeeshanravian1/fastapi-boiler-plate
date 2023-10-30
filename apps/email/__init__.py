"""
    Email Module

    Description:
    - This module is used to send email to user.

"""

from .configuration import email_configuration
from .response_message import email_response_message
from .schema import EmailBaseSchema, EmailSentSchema
from .helper import send_email_otp
