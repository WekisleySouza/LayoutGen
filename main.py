from classes.Test import Test
from classes.ModelDrawer import ModelDrawer


modelDrawer = ModelDrawer()

environment = Test.create_environment(30)

environment.place_objects_ramdomly()

modelDrawer.draw_all(environment)

modelDrawer.save_img()