import sys
from figures import *



def handle_figure(figure):
    try:
        if figure[0] == 'Square':
            fig = Square(figure)
        elif figure[0] == 'Rectangle':
            fig = Rectangle(figure)
        elif figure[0] == 'Circle':
            fig = Circle(figure)
        elif figure[0] == 'Triangle':
            fig = Triangle(figure)
        return f'{fig.__class__.__name__} Perimeter {fig.perimeter()} Area {fig.area()}'
    except ValueError as ec:
        return ec






if __name__ == "__main__":
    input_data = sys.stdin.readlines()
    list_data = [x.split() for x in input_data]

    for figure in list_data:
        handle_figure(figure)



