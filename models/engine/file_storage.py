#!/usr/bin/python3
"""From Uganda"""

import json
from models.base_model import BaseModel


class FileStorage:
    """aaaa"""

    def __init__(self, file_path, objects):
        """aaaa"""

        slef.__fle_path = file_path
        self.__objects = objects

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

        try:
            with open(self.__file_path, mode="r") as f:
                diccionarintin = json.loads(f.read())
                for PEPE, PIPO in diccionrintin.items():
                    self.__object[PEPE] = eval(PIPO["__class__"])(**PIPO)
        except Exception:
            pass
