#!/usr/bin/python3
"""Class HBNBCommand"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import ast
import shlex


class HBNBCommand(cmd.Cmd):
    """Class that handle command line is created"""

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """when presse ctrl + D it exists the command line interpreter"""
        return True

    def emptyline(self):
        """when user enters nothing the loop continues with the prompt"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]
        line = line.strip()
        if not line:
            print("** class name missing **")
            return
        list_ = line.split(" ", 1)
        class_name = list_[0]
        if (class_name in classes):
            cls_object = globals()[class_name]
            new_obj_in = cls_object()
            new_obj_in.save()
            print("{}".format(new_obj_in.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints string representation class name and id"""

        line = line.strip()
        if not line:
            print("** class name missing **")
            return
        list_ = line.split(" ")
        class_name = list_[0]
        if (len(list_) < 2):
            print("** instance id missing **")
            return
        id_ = list_[1]
        Base_model_id = class_name + "." + id_
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        if (class_name not in classes):
            print("** class doesn't exist **")
            return
        objects_ = storage.all()
        for key, value in objects_.items():
            if (key == Base_model_id):
                retrieved_instance = objects_[key]
                print(retrieved_instance)
                return
        print("** no instance found **")

    def destroy_instance(self, id_instance):
        line = id_instance.strip()
        objects_ = storage.all()
        for key, value in objects_.items():
            if (key.split(".")[1] == line):
                objects_.pop(key)
                storage.save()
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        line = line.strip()
        if not line:
            print("** class name missing **")
            return
        list_ = line.split(" ")
        class_name = list_[0]
        if (len(list_) < 2):
            print("** instance id missing **")
            return
        id_ = list_[1]
        Base_model_id = class_name + "." + id_
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        if (class_name not in classes):
            print("** class doesn't exist **")
            return
        objects_ = storage.all()
        for key, value in objects_.items():
            if (key == Base_model_id):
                objects_.pop(key)
                storage.save()
                return
        print("** no instance found **")

    def default(self, line):
        list_of_classes = ["BaseModel", "User", "State",
                           "City", "Amenity", "Place", "Review"]
        line = line.strip()
        if line.find(".") == -1:
            print("** Unkown syntax: {} ***".format(line))
            return
        class_name = line.split(".")[0]
        if class_name not in list_of_classes:
            print("** class name not found **")
            return
        command_part = line.split(".")[1]
        characters = r"[a-zA-Z]+(?=\()"
        specific_command = re.findall(characters, command_part)[0]
        if command_part == "count()":
            count = self.count(class_name)
            if (count != -127):
                print(count)
            else:
                return
        elif specific_command == "show":
            characters_checker = r'(?<=").+(?=")'
            id_ = re.findall(characters_checker, command_part)[0]
            instance = self.show(class_name, id_)
            if instance != -1:
                print(instance)
            else:
                print("** no instance found **")
        elif specific_command == "destroy":
            characters_checker = r'(?<=").+?(?=")'
            id_ = re.findall(characters_checker, command_part)[0]
            self.destroy_instance(id_)
        elif specific_command == "update":
            characters_checker = r'(?<=")[^,].+?(?=")'
            dictionary_checker = r'(?<={).+?(?=})'
            if len(re.findall(dictionary_checker, command_part)) == 1:
                id_ = re.findall(characters_checker, command_part)[0]
                key = re.findall(dictionary_checker, command_part)[0]
                dictionary_string = "{" + key + "}"
                dictionary = ast.literal_eval(dictionary_string)
            else:
                characters_checker = r'(?<=")[^,].+?(?=")|[-+]?\d*\.?\d+'
                dictionary = {}
                id_ = re.findall(characters_checker, command_part)[0]
                """print("I am id {}".format(id_))"""
                value = re.findall(characters_checker, command_part)[2]
                """print("I am value {}".format(value))"""
                key = re.findall(characters_checker, command_part)[1]
                """print("I am key {}".format(key))"""
                dictionary[key] = value
                """print("I am the dictionary {}".format(dictionary))"""

            self.update(class_name, id_, dictionary)

        elif command_part == "all()":
            self.do_all(class_name)
        else:
            print("** Unkown syntax: {} ***".format(line))
            return

    def do_all(self, line):
        """Prints all string representation based or not on the class name. """
        list_of_classes = ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]
        line = line.strip()
        list_ = line.split(" ")
        class_name = list_[0]
        if line:
            if (class_name not in list_of_classes):
                print("** class doesn't exist **")
                return
            list_instances = []
            objects_ = storage.all()
            for key, value in objects_.items():
                if (key.split(".")[0] == class_name):
                    returned_instance = value.__str__()
                    list_instances.append(returned_instance)
        else:
            list_instances = []
            objects_ = storage.all()
            for key, value in objects_.items():
                returned_instance = value.__str__()
                list_instances.append(returned_instance)
        print(list_instances)

    def count(self, line):
        """prints the number of instances of a class"""
        list_of_classes = ["BaseModel", "User", "State",
                           "City", "Amenity", "Place", "Review"]
        if line:
            if (line not in list_of_classes):
                return (-127)
            objects_ = storage.all()
            count = 0
            for key, value in objects_.items():
                if (key.split(".")[0] == line):
                    count = count + 1
        return (count)

    def show(self, class_name, line):
        """Retrieves an instance based on its ID"""
        objects_ = storage.all()
        for key, value in objects_.items():
            if (key.split(".")[0] == class_name):
                if (key.split(".")[1] == line):
                    return (value.__str__())
        return (-1)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        list_of_classes = ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]
        line = line.strip()
        if not line:
            print("** class name missing **")
            return
        list_ = shlex.split(line)
        class_name = list_[0]
        if class_name not in list_of_classes:
            print("** class doesn't exist **")
            return
        if (len(list_) >= 2):
            instance_id = list_[1]
        else:
            print("** instance id missing **")
            return

        key = class_name + "." + instance_id
        objects_ = storage.all()
        if key in objects_:
            instance = objects_[key]
            if (len(list_) >= 3):
                attribute_name = list_[2]
            else:
                print("** attribute name missing **")
                return
            if attribute_name:
                if (len(list_) >= 4):
                    attribute_value = list_[3]
                else:
                    print("** value missing **")
                    return
                if attribute_name in ["id", "created_at", "updated_at"]:
                    return
                if attribute_name in ["number_rooms", "number_bathrooms",
                                      "max_guest", "price_by_night"]:
                    attribute_value = int(attribute_value)
                elif attribute_name in ["latitude", "longitude"]:
                    attribute_value = float(attribute_value)
                """if hasattr(instance, attribute_name):"""
                setattr(instance, attribute_name, attribute_value)
                instance.save()
        else:
            print("** no instance found **")
            return

    def update(self, class_name, id_, dictionary):
        """Updates value based on ID and dictionary"""
        objects_ = storage.all()
        tracker = 0
        for key, value in objects_.items():
            if key.split(".")[1] == id_:
                for k, v in dictionary.items():
                    if k in ["id", "created_at", "updated_at"]:
                        continue
                    if k in ["number_rooms", "number_bathrooms",
                             "max_guest", "price_by_night"]:
                        dictionary[k] = int(v)
                    if k in ["latitude", "longitude"]:
                        dictionary[k] = float(v)
                    setattr(value, k, v)
                    tracker = tracker + 1
                    value.save()
    """
        if (tracker == 0):
            print("** no instance found **")
    """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
