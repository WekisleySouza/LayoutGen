from classes.Shape import Shape
from classes.Door import Door
from random import random

class Environment:
    def __init__(self):
        self.__name = ''
        self.__shape = None
        self.__objects = []
        self.__doors = []

    @property
    def objects_number(self):
        return len(self.__objects)

    @property
    def shape(self):
        return self.__shape
    
    @property
    def objects(self):
        return self.__objects
    
    @property
    def position(self) -> tuple:
        return self.__shape.position
    @property
    def width(self) -> int:
        return self.__shape.width
    
    @property
    def height(self) -> int:
        return self.__shape.height
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def doors(self) -> list:
        return self.__doors

    def add_door(self, door: Door) -> None:
        # door.update_attributes(self.width, self.height)
        self.__doors.append(door)

    def add_shape(self, shape: Shape) -> None:
        self.__shape = shape

    def add_object(self, object: Shape) -> None:
        self.__objects.append(object)

    def copy(self):
        environment = self.__class__()
        environment.add_shape(self.__shape.copy())
        for object in self.__objects:
            environment.add_object(object.copy())
        for door in self.__doors:
            environment.add_door(door.copy())
        return environment

    def has_door_obstructed(self):
        for door in self.__doors:
            for obj in self.objects:
                if obj.colides(door):
                    return True
        return False

    def colides(self, index, object, object_list: list) -> bool:
        for i, obj in enumerate(object_list):
            if object.colides(obj) and i != index:
                return True
        return False

    def place_objects_ramdomly(self):
        for i, obj in enumerate(self.__objects):
            colides = True
            while colides:
                x = abs(round(random() * self.width - obj.width, 2))
                y = abs(round(random() * self.height - obj.height, 2))
                obj.position = (x, y)
                colides = self.colides(i, obj, self.__objects)
        return self