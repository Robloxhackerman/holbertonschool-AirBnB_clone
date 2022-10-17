#!/usr/bin/python3
"""
TLC con china
"""
import datetime
import uuid
import models


class BaseModel:
    """pa despues"""

    def __init__(self, *args, **kwargs):
        """pipo"""

        if kwargs:
            for PEPOS, P in kwargs.items():
                if PEPOS in ("created_at", "updated_at"):
                    P = datetime.datetime.strptime(P, "%Y-%m-%dT%H:%M:%S.%f")
                if PEPOS != "__class__":
                    setattr(self, PEPOS, P)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """pipo"""
        clase = self.__class__.__name__
        return "[{}] ({}) {}".format(clase, self.id, self.__dict__)

    def save(self):
        """pipo"""

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """pipo"""

        diccionaritito = self.__dict__.copy()
        diccionaritito["__class__"] = self.__class__.__name__
        diccionaritito["created_at"] = self.created_at.isoformat()
        diccionaritito["updated_at"] = self.updated_at.isoformat()

        return diccionaritito
