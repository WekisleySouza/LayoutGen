from classes.Rectangle import Rectangle
from classes.Object import Object
from classes.Environment import Environment
from random import random

class Test:
    @staticmethod
    def create_environment(obj_n):
        environment = Environment()
        shape_environment = Rectangle((1, 1), 995.0, 995)
        environment.add_shape(shape_environment)

        for i in range(obj_n):
            w = abs(round(random() * 200))
            h = abs(round(random() * 200))
            shape_obj = Rectangle((2, 2), w, h)
            obj = Object(f'Obj {i+1}')
            obj.add_shape(shape_obj)
            environment.add_object(obj)

        return environment
                
