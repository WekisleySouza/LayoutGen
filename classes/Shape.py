class Shape:
    def __init__(self, shape_type: str, initial_position: tuple) -> None:
        self.__position = initial_position
        self.__shape_type = shape_type

    @property
    def position(self) -> tuple:
        return self.__position
    
    @position.setter
    def position(self, position: tuple) -> tuple:
        self.__position = position
    
    @property
    def type(self) -> str:
        return self.__shape_type
    
    def colides(self) -> bool:
        return True