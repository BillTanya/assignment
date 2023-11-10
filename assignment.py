import sys
from figures import *



def handle_figure(figure):
    try:
        if figure[0] == 'Square':
            square = Square(figure)
            return f'Square Perimeter {square.perimeter()} Area {square.area()}'
        elif figure[0] == 'Rectangle':
            rectangle = Rectangle(figure)
            return f'Rectangle Perimeter {rectangle.perimeter()} Area {rectangle.area()}'
        elif figure[0] == 'Circle':
            circle = Circle(figure)
            return f'Circle Perimeter {circle.perimeter()} Area {circle.area()}'
        elif figure[0] == 'Triangle':
            triangle = Triangle(figure)
            return f'Triangle Perimeter {triangle.perimeter()} Area {triangle.area()}'
    except ValueError as ec:
        return ec





if __name__ == "__main__":
    input_data = sys.stdin.readlines()
    list_data = [x.split() for x in input_data]

    for figure in list_data:
        handle_figure(figure)



