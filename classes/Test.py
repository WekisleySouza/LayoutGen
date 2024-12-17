from classes.Rectangle import Rectangle
from classes.Door import Door
from classes.Object import Object
from classes.Environment import Environment
from classes.GeneticAlgorithm import GeneticAlgorithm
from random import random

class Test:
    @staticmethod
    def create_environment(obj_n):
        environment = Environment()
        shape_environment = Rectangle((1, 1), 995.0, 995)
        door = Door((796.0, 1), 100)
        door2 = Door((40, 955), 100)
        environment.add_shape(shape_environment)
        environment.add_door(door)
        environment.add_door(door2)

        for i in range(obj_n):
            w = abs(round(random() * 200))
            h = abs(round(random() * 200))
            shape_obj = Rectangle((2, 2), w, h)
            obj = Object(f'Obj {i+1}')
            obj.add_shape(shape_obj)
            environment.add_object(obj)

        return environment
                
    @staticmethod
    def genetic_algorithm(population_size=4):
        environment = Test.create_environment(30)
        gna = GeneticAlgorithm(environment, population_size, 12, 12)
        gna.generate_initial_population()
        return gna
