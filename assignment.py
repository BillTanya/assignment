import sys
from figures import *

figure_dict = {
    'Square': Square,
    'Rectangle': Rectangle,
    "Circle": Circle,
    "Triangle": Triangle
}


def handle_figure(figure):
    try:
        fig = figure_dict[figure[0]](figure)
        return f'{fig.__class__.__name__} Perimeter {fig.perimeter()} Area {fig.area()}'
    except ValueError as ec:
        return ec


if __name__ == "__main__":
    input_data = sys.stdin.readlines()
    list_data = [x.split() for x in input_data]

    for figure in list_data:
        handle_figure(figure)



