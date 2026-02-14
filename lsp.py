# class Bird:
#     def fly(self):
#         return "The bird is flying"

#     def walk(self):
#         return "The bird is walking"


# class Duck(Bird):
#     def fly(self):
#         return "The duck is flying"

#     def walk(self):
#         return "The duck is walking"


# class Penguin(Bird):
#     def fly(self):
#         raise AttributeError("Penguins cannot fly:(")

#     def walk(self):
#         return "The penguin is walking"


class FlyingBird():
    def fly():
        return "The bird is flying"

class WalkingBird():
    def walking():
        return "The bird is walking"

class Duck(FlyingBird, WalkingBird):
    def fly():
        return "The duck is flying"

    def walking():
        return "The duck is walking"

class Penguin(WalkingBird):
    def walking():
        return "The penguin is walking"