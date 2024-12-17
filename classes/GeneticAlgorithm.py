from classes.Environment import Environment

class GeneticAlgorithm:
    def __init__(self, environment: Environment, population_size, mutation_rate, crossover_rate):
        self.__population = []
        self.__environment = environment
        self.__population_size = population_size
        self.__mutation_rate = mutation_rate
        self.__crossover_rate = crossover_rate

    @property
    def population(self) -> list:
        return self.__population

    def generate_initial_population(self):
        for i in range(self.__population_size):
            env = self.__environment.copy().place_objects_ramdomly()
            env.name = f'Env(1-{i+1})'
            self.__population.append(env)

    def fitness_function(self):
        for env in self.__population:
            if env.has_door_obstructed():
                return True
        return False