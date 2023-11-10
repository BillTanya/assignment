import unittest
from figures import Square, Rectangle, Circle, Triangle
from assignment import handle_figure


class SquareTest(unittest.TestCase):
    valid_data = [
        [["Square", "TopRight", "2", "2", "Side", "2"], 8, 4],
        [["Square", "TopRight", "3", "2", "Side", "3"], 12, 9],
        [["Square", "TopRight", "2", "2", "Side", "4"], 16, 16]]
    not_valid_data = [
        ["Square", "TopRight", "2", "2", "Side", "0"],
        ["Square", "TopRight", "2", "2", "Side", "-2"],
        ["Square", "TopRight", "2", "2", "Side"]]

    def test_perimeter(self):
        for data in self.valid_data:
            s = Square(data[0])
            self.assertEqual(s.perimeter(), data[1])

    def test_area(self):
        for data in self.valid_data:
            s = Square(data[0])
            self.assertEqual(s.area(), data[2])

    def test_not_valid_data(self):
        with self.assertRaises(ValueError) as ec:
            for data in self.not_valid_data:
                s = Square(data)


class RectangleTest(unittest.TestCase):
    valid_data = [
        [[3, 3, 1, 1], 8, 4],
        [[5, 4, 0, 0], 18, 20],
        [[4, 2, 1, 1], 8, 3],
        [[1, 1, -2, -2], 12, 9]]
    not_valid_data = [
        [3, 3, 5, 1],
        [2, 4, 4, 0],
        [3, 3, 3, 3]]

    def test_perimeter(self):
        for data in self.valid_data:
            r = Rectangle(*data[0])
            self.assertEqual(r.perimeter(), data[1])

    def test_area(self):
        for data in self.valid_data:
            r = Rectangle(*data[0])
            self.assertEqual(r.area(), data[-1])

    def test_not_valid_data(self):
        with self.assertRaises(ValueError) as ec:
            for data in self.not_valid_data:
                r = Rectangle(*data)


class CircleTest(unittest.TestCase):
    valid_data = [
        [[1, 1, 3], 18.85, 28.27],
        [[1, 2, 4], 25.13, 50.27],
        [[1, 1, 5], 31.42, 78.54]]
    not_valid_data = [
        [1, 1, 0],
        [1, 2, -2],
        [1, 1, -4]]

    def test_perimeter(self):
        for data in self.valid_data:
            c = Circle(*data[0])
            self.assertEqual(c.perimeter(), data[1])

    def test_area(self):
        for data in self.valid_data:
            c = Circle(*data[0])
            self.assertEqual(c.area(), data[2])

    def test_not_valid_data(self):
        with self.assertRaises(ValueError) as ec:
            for data in self.not_valid_data:
                c = Circle(*data)


class TriangleTest(unittest.TestCase):
    valid_data = [
        [[5, 4, 3, 2, 6, 8], 13.66, 3],
        [[4, 4, 2, 2, 8, 2], 13.3, 6],
        [[5, 4, 1, 1, 10, 4], 19.49, 7.5]]
    not_valid_data = [
        [5, 5, 5, 6, 5, 9],
        [4, 4, 4, 4, 8, 2]]

    def test_perimeter(self):
        for data in self.valid_data:
            t = Triangle(*data[0])
            self.assertAlmostEqual(t.perimeter(), data[1], delta=0.1)

    def test_area(self):
        for data in self.valid_data:
            t = Triangle(*data[0])
            self.assertAlmostEqual(t.area(), data[2], delta=0.1)

    def test_not_valid_data(self):
        with self.assertRaises(ValueError) as ec:
            for data in self.not_valid_data:
                t = Triangle(*data)


class HandleFigureTest(unittest.TestCase):
    def test_data(self):
        figure = ["Square", "TopRight", "1", "1", "Side", "1"]
        valid_data = 'Square Perimeter 4 Area 1'
        self.assertEqual(handle_figure(figure), valid_data)

