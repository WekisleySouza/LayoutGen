from classes.Test import Test
from classes.ModelDrawer import ModelDrawer

gna = Test.genetic_algorithm(1)

print(gna.fitness_function())

for env in gna.population:
    modelDrawer = ModelDrawer()
    
    modelDrawer.draw_all(env)
    modelDrawer.name = env.name

    modelDrawer.save_img()