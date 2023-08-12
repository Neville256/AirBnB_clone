
#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, **kwargs):
        """Public instance attributes initialization after creation"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            self.__update_from_dict(kwargs)

    def __update_from_dict(self, kwargs):
        for key, value in kwargs.items():
            if key in ("updated_at", "created_at"):
                setattr(self, key, datetime.strptime(value, self.DATE_TIME_FORMAT))
            elif key == "id":
                setattr(self, key, str(value))
            else:
                setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """Return a string representation of the class. """

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        mapped_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                mapped_objects[key] = value.isoformat()
            else:
                mapped_objects[key] = value
        mapped_objects["__class__"] = self.__class__.__name__
        return mapped_objects
