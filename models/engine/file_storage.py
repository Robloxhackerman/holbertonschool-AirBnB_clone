#!/usr/bin/python3
"""From Uganda"""

import json
from models.base_model import BaseModel
from models.user import User
from os import path


class FileStorage:
    """aaaa"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """aaa"""

        return self.__objects

    def new(self, obj):
        """aaa"""

        CHICHO = obj.__class__.__name__ + "." + obj.id
        self.__objects[CHICHO] = obj

    def save(self):
        """aaa"""

        diccionarin = {}

        for PEPE, PIPO in self.__objects.items():
            diccionarin[PEPE] = PIPO.to_dict()
        with open(self.__file_path, mode="w") as f:
            f.write(json.dumps(diccionarin))

    def reload(self):
        """aaaaa"""

        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                diccionarintin = json.loads(f.read())
                for PEPE in diccionarintin.values():
                    clasesita = PEPE["__class__"]
                    self.new(eval(clasesita)(**PEPE))
