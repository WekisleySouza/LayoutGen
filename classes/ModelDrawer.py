from PIL import Image, ImageDraw

from data.ShapeTypes import ShapeTypes
from classes.Shape import Shape
from classes.Environment import Environment

class ModelDrawer():
    def __init__(self, width=1000, heigth=1000, color='white', name='model') -> None:
        self.__name = name
        self.__model_img = Image.new('RGB', (width, heigth), color)
        self.__draw = ImageDraw.Draw(self.__model_img)

    def draw(self, shape: Shape, text='', color='black', width=3) -> None:
        x, y = shape.position
        if shape.type == ShapeTypes.RECTANGLE:
            self.__draw.rectangle([x, y, shape.width + x, shape.height + y], outline=color, width=width)
            self.__draw.text((x+5, y+5), text, fill=color)

    def draw_all(self, environment: Environment):
        self.draw(environment.shape, color='red')
        for obj in environment.objects:
            self.draw(obj.shape, text=obj.name)

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def save_img(self) -> None:
        self.__model_img.save(f"./images/{self.__name}.png", "png")

