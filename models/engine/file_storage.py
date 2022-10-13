#!/usr/bin/python3
"""From Uganda"""

import json
from models.base_model import BaseModel
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
        
        diccionarintin = {}

        if path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                diccionarintin = json.loads(f.read())
                for PEPE, PIPO in diccionrintin.items():
                    self.__object[PEPE] = eval(PIPO["__class__"])(**PIPO)
