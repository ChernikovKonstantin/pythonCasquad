#from Poly_figures import Rectangle, Square
from Lessons.Poly_figures import Rectangle, Square, Rectangle_Poly, Square_poly


class Area(Rectangle, Square):
    rect1 = Rectangle(3,5)
    rect2 = Rectangle(3,6)

    #print(rect1.get_area_rec(),rect2.get_area_rec())

    square1 = Square(10)
    square2 = Square(5)

    #print(square1.get_area_sq(), square2.get_area_sq())

    figures = [rect1,rect2,square1,square2]
    for figure in figures:
        if isinstance(figures,Rectangle):
            print(figure.get_area_rec())
        elif isinstance(figures, Square):
            print(figure.get_area_sq())

class Area_Polymorphism(Rectangle_Poly, Square_poly):
    rect1 = Rectangle_Poly(3,5)
    rect2 = Rectangle_Poly(3,6)


    square1 = Square_poly(10)
    square2 = Square_poly(5)

    print(rect1.get_area(),rect2.get_area(),square1.get_area(),square2.get_area())

    figures = [rect1, rect2, square1, square2]


    for figure in figures:
        print(figure.get_area())





