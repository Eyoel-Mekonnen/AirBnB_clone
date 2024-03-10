#!/usr/bin/python3


"""Class BaseModel that defines attribute/methods of other classes"""
import models
from datetime import datetime
import uuid



class BaseModel:
    """Class BaseModel has been defined"""
    def __init__(self, *args, **kwargs):
        """the object is being instancated"""


        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                elif(key == "id"):
                    self.id = value
                elif(key == "created_at"):
                    date_object = datetime.strptime(value, time_format)
                    self.created_at = date_object
                elif(key == "updated_at"):
                    date_object = datetime.strptime(value, time_format)
                    self.updated_at = date_object
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """__str__ will return class name, self.id and self.__dict__"""

        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the updated time with now"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """creating a dictionary with __class__ key and instance attributes"""

        class_name_ = self.__class__.__name__
        dict_name = {"__class__": class_name_}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_name[key] = value.isoformat()
            else:
                dict_name[key] = value
        return (dict_name)

