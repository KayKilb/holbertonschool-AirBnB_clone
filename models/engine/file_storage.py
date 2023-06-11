#!/usr/bin/python3
import json
import os
"""
Write a class FileStorage
that serializes instances
to a JSON file and deserializes
JSON file to instances
"""


class FileStorage:
    """Serializes and deserializes instances"""
    __file_path = "saved.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds an obj and its key in the dict"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to __file_path"""
        with open(FileStorage.__file_path, "w") as f:
            out = {}
            for key, value in FileStorage.__objects.items():
                out[key] = value.to_dict()
            json.dump(out, f)

    def reload(self):
        """Deserializes __file_path to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
