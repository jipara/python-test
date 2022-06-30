def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2, 3, 6))


## **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
        #print(value)
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=2)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

        #or

        self.make = kwargs.get("make")
        self.make = kwargs.get("model")

my_car = Car(make="Toyota", model="Camry")
print(my_car.model)
