#!/usr/bin/python3
"""
TLC con china
"""
import datetime
import uuid


class BaseModel:
    """pa despues"""

    def __init__(self):
        """pipo"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """pipo"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """pipo"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """pipo"""

        diccionaritito = self.__dict__.copy()
        diccionaritito["__class__"] = self.__class__.__name__
        diccionaritito["created_at"] = self.created_at.isoformat()
        diccionaritito["updated_at"] = self.updated_at.isoformat()
