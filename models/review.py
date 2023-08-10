#!/usr/bin/python3
"""Defines a module."""


from models.base_model import BaseModel
"""Import modules."""


class Review(BaseModel):
    """Create a new class review inheriting from basemodel."""
    place_id = ""
    user_id = ""
    text = ""
