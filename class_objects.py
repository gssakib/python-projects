## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## A class named Dog inherits(is-a) from another class named Animal 
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a attribute named name
        self.name = name

## A class named Cat inherits(is-a) from another class named Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a attribute named name
        self.name = name

## A class named Person inherits(is-a) from a class named object
class Person(object):

    def __init__(self, name):
        ##class Person has-a attribute named name
        self.name = name

        ## class Person has-a attribut named pet whose value is None
        self.pet = None

## Class Employee inherits(is-a) from a class named Person
class Employee(Person):

    def __init__(self, name, salary):
        ## class Employee has-a function named ?????
        super(Employee, self).__init__(name)
        ## class Employee has-a attribute named salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a attribute named pet whose is satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## class frank has-a attribute named pet whose value is rover
frank.pet = rover

## flipper is an instance of Fish
flipper = Fish()

## crouse is an instance of Salmon
crouse = Salmon()

## harry is an instance of Halibut
harry = Halibut()