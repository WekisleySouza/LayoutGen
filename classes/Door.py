from classes.Rectangle import Rectangle

class Door(Rectangle):
    def __init__(self, initial_position: tuple, width: int) -> None:
        super().__init__(initial_position, width, 40)
        self.__name = 'Door'

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def update_attributes(self, w_e, h_e):
        x, y = self.position
        w, h = self.width, self.height
        if x == 1 or x == 1 + w_e:
            self.position = (x - self.height - 50, y)
            super().swap_dimensions()


    def copy(self):
        return self.__class__(self.position, self.width)