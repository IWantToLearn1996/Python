def add(*args):
    print(sum(args))
    print(args[0])

    # sum2 = 0
    # for num in args:
    #     sum2 += num
    # return sum2

add(3, 5, 6, 2, 1)

def calculate(n, **kwargs):
    #print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    # takes n and adds the add which is 3 so 2+3=5
    n += kwargs["add"]
    # takes the 5 from above and multiplies it with 5 so 5*5=25
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)

class Car2:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car2 = Car2(color="Red")
print(my_car2.color)
