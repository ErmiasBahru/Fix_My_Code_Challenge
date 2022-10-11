#!/usr/bin/python3
"""Class Square
Defines a squaare geometry
"""


class Square:
    """
    Defines square geometry
    """

    def __init__(self, *args, **kwargs):
        """Initializes the Square class
        Args:
            args: arguments passed on instance
            kwargs: keyword arguments passes on instance
        Attributes:
            width (int): the width of the square
            height (int): the height of the square
        """
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
