"""
    FastAPI Route module

    Description:
    - This module is used to create routes for application.

"""

# Importing Python Packages

# Importing FastAPI Packages
from fastapi import APIRouter

# Importing Project Files
from apps import v1_routers


# Router Object to Create Routes
router = APIRouter()


# -----------------------------------------------------------------------------


# Include all file routes
router.include_router(v1_routers)
