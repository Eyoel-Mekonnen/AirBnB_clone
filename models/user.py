#!/usr/bin/python3
"""class User is being created"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class user created that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

