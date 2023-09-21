"""
    User Model

    Description:
    - This file contains model for user table.

"""

# Importing Python Packages
from sqlalchemy import Boolean, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# Importing FastAPI Packages

# Importing Project Files
from database import BaseTable
from ..role.model import RoleTable


# -----------------------------------------------------------------------------


class UserTable(BaseTable):
    """
    User Table

    Description:
    - This table is used to create user in database.

    """

    first_name: Mapped[str] = mapped_column(String(2_55))
    last_name: Mapped[str] = mapped_column(String(2_55))
    contact: Mapped[str] = mapped_column(String(2_55), nullable=True)
    username: Mapped[str] = mapped_column(String(2_55), unique=True)
    email: Mapped[str] = mapped_column(String(2_55), unique=True)
    password: Mapped[str] = mapped_column(String(2_55))
    address: Mapped[str] = mapped_column(String(2_55), nullable=True)
    city: Mapped[str] = mapped_column(String(2_55), nullable=True)
    state: Mapped[str] = mapped_column(String(2_55), nullable=True)
    country: Mapped[str] = mapped_column(String(2_55), nullable=True)
    postal_code: Mapped[str] = mapped_column(String(2_55), nullable=True)
    profile_image_path: Mapped[str] = mapped_column(
        String(2_55), nullable=True
    )
    email_otp: Mapped[str] = mapped_column(String(2_55), nullable=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    password_otp: Mapped[str] = mapped_column(String(2_55), nullable=True)
    password_verified: Mapped[bool] = mapped_column(Boolean, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    role_id: Mapped[int] = mapped_column(ForeignKey(RoleTable.id))
