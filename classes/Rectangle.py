from classes.Shape import Shape
from data.ShapeTypes import ShapeTypes

class Rectangle(Shape):
    def __init__(self, initial_position: tuple, width: int, height: int) -> None:
        super().__init__(ShapeTypes.RECTANGLE, initial_position)
        self.__width = width
        self.__height = height

    @property
    def width(self) -> None:
        return self.__width
    
    @property
    def height(self) -> None:
        return self.__height
    
    def colides(self, rectangle) -> None:
        x, y = rectangle.position
        self_x, self_y = self.position
        final_self_x = self.width + self_x
        final_self_y = self.height + self_y
        final_x = rectangle.width + x
        final_y = rectangle.height + y

        if final_self_x < x or self_x > final_x:
            return False
        if final_self_y < y or self_y > final_y:
            return False
        return True