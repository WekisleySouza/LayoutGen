from classes.Shape import Shape

class Object:
    def __init__(self, name) -> None:
        self.__shape = None
        self.__name = name

    @property
    def shape(self):
        return self.__shape
    
    @property
    def name(self):
        return self.__name
    
    @property
    def position(self) -> tuple:
        return self.__shape.position
    
    @position.setter
    def position(self, position: tuple) -> tuple:
        self.__shape.position = position
    
    @property
    def width(self) -> int:
        return self.__shape.width
    
    @property
    def height(self) -> int:
        return self.__shape.height

    def add_shape(self, shape: Shape) -> None:
        self.__shape = shape

    def colides(self, object) -> bool:
        return self.__shape.colides(object)
    
    