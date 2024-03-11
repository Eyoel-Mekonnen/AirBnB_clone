#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model_ = BaseModel()
my_model_.name = "My_Second_Model"
my_model_.my_number = 5555
my_model_.save()
print(my_model_)
