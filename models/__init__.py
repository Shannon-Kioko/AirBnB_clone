#!/usr/bin/python3
"""
This module conatins the instantiation of the FileStorage class
"""
# models/__init__.py

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
