class cat():
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("My name is ", self.name)
        print("meow meow")

class dog():
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("My name is ", self.name)
        print("bow bow")

cat1=cat("ASH")
dog1=dog("yoentan")

for animal in (dog1,cat1):
    animal.make_sound()
    