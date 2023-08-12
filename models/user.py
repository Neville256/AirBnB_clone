#!/usr/bin/python3
"""Defines a module."""


from models.base_model import BaseModel
"""Import modules."""


class User(BaseModel):
    """Create a new class user inheriting from basemodel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
