class Bird:
    def fly(self):
        return "The bird is flying"

    def walk(self):
        return "The bird is walking"


class Duck(Bird):
    def fly(self):
        return "The duck is flying"

    def walk(self):
        return "The duck is walking"


class Penguin(Bird):
    def fly(self):
        raise AttributeError("Penguins cannot fly:(")

    def walk(self):
        return "The penguin is walking"
