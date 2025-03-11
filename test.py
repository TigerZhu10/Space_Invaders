
class Animals():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        print(f"{self.name} make noise")


dog = Animals("Kevin", "red")
dog.sound()