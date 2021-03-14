#!/usr/bin/python3
"""
base module
"""
import json
import csv


class Base:
    """
    base class
    """
    __nb_obj = 0

    def __init__(self, id=None):
        """ init class  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_obj += 1
            self.id = Base.__nb_obj

    @classmethod
    def save_to_file(cls, list_objs: list):
        """
        create a json file
        """
        className = cls.__name__ + ".json"
        with open(className, mode="w") as file:
            if list_objs is None:
                list_objs = []
            newJson = [inst.to_dictionary() for inst in list_objs]
            file.write(cls.to_json_string(newJson))

    def from_json_string(json_string):
        """
            transform a string
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
            create new instance
        """
        dummy = cls(55, 66)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass

    @classmethod
    def load_from_file(cls):
        """
            open file and read all contents
        """
        className = cls.__name__ + ".json"
        arAttrs = []
        try:
            with open(className, mode="r") as file:
                content = file.read()
                listOfDicts = cls.from_json_string(content)
                for instDict in listOfDicts:
                    newInst = cls.create(**instDict)
                    arAttrs.append(newInst)
                return arAttrs
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method transform list of dict to str
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write file
        """
        className = cls.__name__ + ".csv"
        with open(className, 'w', encoding="utf8") as csvfile:
            if list_objs is None:
                list_objs = []
            if cls.__name__ == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=attrs)
            for inst in list_objs:
                writer.writerow(inst.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            list of instance
        """
        className = cls.__name__ + ".csv"
        result = []
        try:
            with open(className, mode="r", encoding="utf8") as csvfile:
                if cls.__name__ == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attrs = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=attrs)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                    result.append(cls.create(**row))
                return result
        except FileNotFoundError:
            return result
