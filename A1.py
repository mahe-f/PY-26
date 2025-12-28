from abc import ABC , abstractmethod

class class1(ABC):
    def print(self,x):
        print("value: ",x)

    @abstractmethod

    def task(self):
        print("We are in abstract method")

class testclass(class1):
    def task(self):
        print("we are inside testclass task")

obj=testclass()
obj.task()
obj.print(100)