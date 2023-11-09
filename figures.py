from math import sqrt, pi


class Square:
    def __init__(self, top_right_x, top_right_y, side):
        self.top_right_x, self.top_right_y = top_right_x, top_right_y
        if side <= 0:
            raise ValueError("The side of the square must be a positive number!")
        self.side = side

    def perimeter(self):
        p = self.side * 4
        return p

    def area(self):
        a = self.side * self.side
        return a


class Rectangle:
    def __init__(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        self.top_right_x, self.top_right_y = top_right_x, top_right_y
        if bottom_left_x >= self.top_right_x or bottom_left_y >= self.top_right_y:
            raise ValueError("The coordinates of the bottomleft point cannot be to "
                             "the right or above the toprigh point!")
        self.bottom_left_x, self.bottom_left_y = bottom_left_x, bottom_left_y
        self.get_top_left_point()

    def perimeter(self):
        p = (sqrt(((self.top_right_x - self.top_left_x)**2 + (self.top_right_y - self.top_left_y)**2)) +
             sqrt(((self.top_left_y - self.bottom_left_y)**2 + (self.top_left_x - self.bottom_left_x)**2))) * 2
        return int(p)

    def area(self):
        a = (sqrt(((self.top_right_x - self.top_left_x)**2 + (self.top_right_y - self.top_left_y)**2)) *
             sqrt(((self.top_left_y - self.bottom_left_y)**2 + (self.top_left_x - self.bottom_left_x)**2)))
        return int(a)

    def get_top_left_point(self):
        self.top_left_x, self.top_left_y = self.bottom_left_x, self.top_right_y


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x, self.center_y = center_x, center_y
        if radius <= 0:
            raise ValueError('The radius of the circle must be a positive number!')
        self.radius = radius

    def perimeter(self):
        p = 2 * pi * self.radius
        return round(p, 2)

    def area(self):
        a = pi * (self.radius * self.radius)
        return round(a, 2)


class Triangle:
    def __init__(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        self.point_1_x = point_1_x
        self.point_1_y = point_1_y
        self.point_2_x = point_2_x
        self.point_2_y = point_2_y
        self.point_3_x = point_3_x
        self.point_3_y = point_3_y
        self.check_valid_triangle(*self.sides_of_the_triangle())

    def sides_of_the_triangle(self):
        self.side_1 = round(sqrt(((self.point_2_x - self.point_1_x)**2 +
                                  (self.point_2_y - self.point_1_y)**2)), 2)
        self.side_2 = round(sqrt(((self.point_3_x - self.point_1_x)**2 +
                                  (self.point_3_y - self.point_1_y)**2)), 2)
        self.side_3 = round(sqrt(((self.point_3_x - self.point_2_x)**2 +
                                  (self.point_3_y - self.point_2_y)**2)), 2)
        return self.side_1, self.side_2, self.side_3

    def perimeter(self):
        p = self.side_1 + self.side_2 + self.side_3
        return round(p, 2)

    def area(self):
        p = self.perimeter() / 2
        a = sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))
        return round(a, 2)

    @staticmethod
    def check_valid_triangle(a, b, c):
        if a + b <= c or a + c <= b or c + b <= a or a == 0 or b == 0 or c == 0:
            raise ValueError('The sum of the lengths of two sides of a triangle '
                             'must be greater than the length of the third side!')





