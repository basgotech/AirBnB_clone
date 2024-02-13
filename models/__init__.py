#!/usr/bin/python3
"""
initialize the models package for storage CRUD.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
