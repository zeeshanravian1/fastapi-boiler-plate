"""
    User Pydantic Schemas

    Description:
    - This module contains all user schemas used by API.

"""

# Importing Python Packages
from pydantic import BaseModel, EmailStr, Field, validator
from pydantic_settings import SettingsConfigDict

# Importing FastAPI Packages

# Importing Project Files
from apps.base import BaseReadSchema, BasePaginationReadSchema
from .configuration import user_configuration, UserTokenStatus
from .helper import (
    names_validator,
    contact_validator,
    username_validator,
    lowercase_email,
    password_validator,
)


# -----------------------------------------------------------------------------


class UserBaseSchema(BaseModel):
    """
    User Base Schema

    Description:
    - This schema is used to validate user base data passed to API.

    """

    first_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.FIRST_NAME,
    )
    first_name_validator = validator("first_name", allow_reuse=True)(
        names_validator
    )
    last_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.LAST_NAME,
    )
    last_name_validator = validator("last_name", allow_reuse=True)(
        names_validator
    )
    contact: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.CONTACT,
    )
    contact_validator = validator("contact", allow_reuse=True)(
        contact_validator
    )
    username: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.USERNAME,
    )
    username_validator = validator("username", allow_reuse=True)(
        username_validator
    )
    email: EmailStr | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.EMAIL,
    )
    email_validator = validator("email", allow_reuse=True)(lowercase_email)
    address: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.ADDRESS,
    )
    city: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.CITY,
    )
    state: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.STATE,
    )
    country: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.COUNTRY,
    )
    postal_code: str | None = Field(
        default=None,
        min_length=1,
        max_length=2_55,
        example=user_configuration.POSTAL_CODE,
    )
    role_id: int | None = Field(
        default=None,
        ge=1,
        example=user_configuration.ROLE_ID,
    )

    # Settings Configuration
    model_config = SettingsConfigDict(
        str_strip_whitespace=True, from_attributes=True
    )


class UserCreateSchema(UserBaseSchema):
    """
    User create Schema

    Description:
    - This schema is used to validate user creation data passed to API.

    """

    first_name: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.FIRST_NAME,
    )
    last_name: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.LAST_NAME,
    )
    username: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.USERNAME,
    )
    email: EmailStr = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.EMAIL,
    )
    password: str = Field(
        min_length=8,
        max_length=1_00,
        example=user_configuration.PASSWORD,
    )
    password_validator = validator("password", allow_reuse=True)(
        password_validator
    )
    role_id: int = Field(
        ge=1,
        example=user_configuration.ROLE_ID,
    )


class UserReadSchema(UserBaseSchema, BaseReadSchema):
    """
    User Read Schema

    Description:
    - This schema is used to validate user data returned from API.

    """

    is_active: bool = Field(example=user_configuration.IS_ACTIVE)
    token_status: UserTokenStatus = Field(example=UserTokenStatus.LOGOUT)


class UserPaginationReadSchema(BasePaginationReadSchema):
    """
    User Pagination Read Schema

    Description:
    - This schema is used to validate user pagination data returned from API.

    """

    records: list[UserReadSchema]


class UserUpdateSchema(UserBaseSchema):
    """
    User Update Schema

    Description:
    - This schema is used to validate user update data passed to API.

    """

    first_name: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.FIRST_NAME,
    )
    last_name: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.LAST_NAME,
    )
    username: str = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.USERNAME,
    )
    email: EmailStr = Field(
        min_length=1,
        max_length=2_55,
        example=user_configuration.EMAIL,
    )
    role_id: int = Field(
        ge=1,
        example=user_configuration.ROLE_ID,
    )
    is_active: bool = Field(example=user_configuration.IS_ACTIVE)


class UserPartialUpdateSchema(UserBaseSchema):
    """
    User Update Schema

    Description:
    - This schema is used to validate user update data passed to API.

    """

    is_active: bool | None = Field(
        default=None, example=user_configuration.IS_ACTIVE
    )


class PasswordChangeSchema(BaseModel):
    """
    Change Password Schema

    Description:
    - This schema is used to validate change password data passed to API.

    """

    old_password: str = Field(
        min_length=8, max_length=1_00, example=user_configuration.PASSWORD
    )
    old_password_validator = validator("old_password", allow_reuse=True)(
        password_validator
    )
    new_password: str = Field(
        min_length=8, max_length=1_00, example=user_configuration.PASSWORD
    )
    new_password_validator = validator("new_password", allow_reuse=True)(
        password_validator
    )

    # Settings Configuration
    model_config = SettingsConfigDict(
        str_strip_whitespace=True, from_attributes=True
    )
