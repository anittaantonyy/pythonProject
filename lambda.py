# x = lambda a : a + 20
# print(x(5))
# x = lambda a , b : a * b
# print(x(3,10))

# class students:
#      # student_name= 'anju'
#     def __init__(self,course,mark):
#       self.course=course
#       self.mark=mark
#     def show(self):
#          print('student:',self.course,self.mark)
#  student1=students("bca",98)
#  student1.show()
#  student2=students("bsc",98)
#  student2.show()


# class Employee:
#     company_name = 'ABC Company'
#     def __init__(self, name, salary):
#         # instance variables
#         self.name = name
#         self.salary = salary
#     def show(self):
#         print('Employee:', self.name, self.salary, self.company_name)
# emp1 = Employee("Harry", 12000)
# emp1.show()
#
# emp2 = Employee("Emma", 10000)
# emp2.show()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#     def show(self):
#         print("Name is ", self.name, "and salary is", self.__salary)
#
# emp = Employee("Jessa", 40000)
# emp.show()
# print(emp.name)

# class Vehicle:
#
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def info(self):
#         print(self.name, self.color, self.price)
#
# # Child class
# class Car(Vehicle):

#     def change_gear(self, no):
#         print(self.name, 'change gear to number', no)
#
# # Create object of Car
# car = Car('BMW X1', 'Black', 35000)
# car.info()
# car.change_gear(5)

class bird:
    def __init__(self, name, wings, price):
        self.name = name
        self.wings = wings
        self.price = price

    def info(self):
            print(self.name, self.wings, self.price)
class parrot(bird):
    def color(self,color):
        print(self.name,'change color')
parrot = parrot("parrot","green",3900)
parrot.info()
parrot.color("red")

