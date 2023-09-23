"""
    FastAPI V1 Route module

    Description:
    - This module is used to create v1 routes for application.

"""

# Importing Python Packages

# Importing FastAPI Packages
from fastapi import APIRouter

# Importing Project Files
from .organization import organization_router
from .role import role_router
from .user import user_router


# Router Object to Create Routes
router = APIRouter(prefix="/v1")


# -----------------------------------------------------------------------------


# Include all file routes
router.include_router(organization_router)
router.include_router(role_router)
router.include_router(user_router)
