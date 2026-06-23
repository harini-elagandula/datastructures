# single inheritance
class parent:
    def land(self):
        print("i have 10 acres of land")
class child(parent):
    pass
obj =child()
obj.land() 


# multiple inheritance 
class parent1:
    def land(self):
        print("i have 10 acres of land")

class parent2:
    def gold(self):
        print("i have 10kgs of gold")   
        
class child(parent1,parent2):
    pass
obj =child()
obj.land() 
obj.gold() 


# polymorphisum
class A:
    def a(self): # method 
        print("welcome")
        
class B(A):
    def a(self): 
        print("good bye")
class C(B):
    def a(self): 
        print("get lost")

obj = C()
obj.a()

# encapsulation:
# public, private, protected, default, static
# types are attribute and method encapsulation; they apply to class data

class Bank:
    def __admin(self):# def __admin is used for name mangling (private method)
        print("amount is:", 1000)
        
obj = Bank()
obj._Bank__admin() # output because of name mangling


# abstraction:
from abc import ABC,abstractmethod
class Bike (ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def acc(self):
        pass
class Bullet(Bike):
    def engine(self):
        print("it has 1000cc of engine")
    def acc(self):
        print("it can pickup in 1.2 sec")
    
gt= Bullet()
gt.engine()