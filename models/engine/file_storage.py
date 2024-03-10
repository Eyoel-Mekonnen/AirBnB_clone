#!/usr/bin/python3
"""Creates the class file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """class is created here"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        object_id = obj.__class__.__name__ + "." + getattr(obj, "id")
        FileStorage.__objects[object_id] = obj

    def save(self):
        """"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """"""
        json_file = {}
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                json_file = json.loads(f.read())
        except FileNotFoundError:
            pass
        for key, value in json_file.items():
            cls_name = key.split(".")[0]
            cls_object = globals().get(cls_name)
            value.pop('__class__')
            obj_creation = cls_object(**value)
            self.new(obj_creation)
