# class shape:
#     def __init__(self, color):
#         self.color = color
#     def draw(self):
#         return f"Drawing a shape with color {self.color}"
# class rectangle(shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#     def draw(self):
#         return super().draw() + f", width {self.width} and height {self.height}"
# def main():
#     rect = rectangle("red", 10, 5)
#     print(rect.draw())
# if __name__ == "__main__":
#     main()
from abc import ABC, abstractmethod
class Hinh(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def draw(self):
        pass
class rectangle(Hinh):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def draw(self):
        return f"Drawing a {self.color} rectangle with width {self.width} and height {self.height}"
def main():
    rect = rectangle("blue", 15, 34)
    print(rect.draw())  
if __name__ == "__main__":
    main()