from classes.Shape import Shape
from random import random

class Environment:
    def __init__(self):
        self.__shape = None
        self.__objects = []

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
    
    def add_shape(self, shape: Shape) -> None:
        self.__shape = shape

    def add_object(self, object: Shape) -> None:
        self.__objects.append(object)

    def __colides(self, index, object, object_list: list) -> bool:
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
                colides = self.__colides(i, obj, self.__objects)