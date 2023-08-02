


class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    def get_area_rec(self):
        area = self.a*self.b
        return area

class Square:
    def __init__(self,a):
        self.a = a

    def get_area_sq(self):
        area = self.a**2
        return area


class Rectangle_Poly:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    def get_area(self):
        area = self.a*self.b
        return area

class Square_poly:
    def __init__(self,a):
        self.a = a

    def get_area(self):
        area = self.a**2
        return area
