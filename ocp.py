from math import pi
from abc import ABC, abstractmethod


class Shape3D():
    @abstractmethod
    def volume(self):
        raise NotImplementedError

class Parallelepiped(Shape3D):
    def __init__(self, w, h, l):
        self.w, self.h, self.l = w, h, l

    def volume(self):
        return self.w * self.h * self.l
    
class Sphere(Shape3D):
    def __init__(self, r):
        self.r = r
    
    def volume(self):
        return 3 / 4 * pi * self.r ** 3
    
class Cone(Shape3D):
    def __init__(self,r,h):
        self.r,self.h = r, h
 
    def volume(self):
        return 1/3 * pi * self.r**2 * self.h
 

# class Shape3D:
#     def __init__(self, shape_type: str, **kwargs):
#         self.shape_type = shape_type
#         self.kwargs = kwargs

#     def calculate_parallelepiped_volume(self):
#         return self.kwargs['w'] * self.kwargs['h'] * self.kwargs['l']

#     def calculate_sphere_volume(self):
#         return 3 / 4 * pi * self.kwargs['r'] ** 3

#     def calculate_cone_volume(self):
#         return 1 / 3 * pi * self.kwargs['r'] ** 2 * self.kwargs['h']

#     def volume(self) -> float:
#         if self.shape_type == 'parallelepiped':
#             return self.calculate_parallelepiped_volume()
#         if self.shape_type == 'sphere':
#             return self.calculate_sphere_volume()
#         if self.shape_type == 'cone':
#             return self.calculate_cone_volume()
#         # Add more ifs forever
#         raise ValueError

# if __name__ == '__main__':
#     print(Shape3D('parallelepiped', w=1.0, h=2.0, l=3.0).volume())
#     print(Shape3D('sphere', r=3.5).volume())
#     print(Shape3D('cone', r=3.5, h=2.0).volume())

if __name__ == '__main__':
    print(Parallelepiped(w=1.0, h=2.0, l=3.0).volume())
    print(Sphere(r=3.5).volume())
    print(Cone(r=3.5, h=2.0).volume())