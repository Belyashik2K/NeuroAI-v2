import asyncio

from .database import mailing_db # Importing mailing_db from mailing/database/__init__.py
from .mailing import mailing_router # Importing mailing_router from mailing/mailing.py
from .tests import UnitTests

asyncio.run(mailing_db.create_tables()) # Creating tables in database

tests = UnitTests() # Initialize UnitTests

__all__ = ["mailing_router"] # Exporting mailing_router