#!/usr/bin/python3
"""Defines a module."""


from models.base_model import BaseModel
"""Import modules."""


class City(BaseModel):
    """Create a new class city inheriting from basemodel."""
    state_id = ""
    name = ""
