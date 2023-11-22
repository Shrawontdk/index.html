class Person:
    name=''
    def getName(self):
        return self.name
    def setName(self, new_name):
        self.name= new_name
    def __str__(self) :
       return "hello"

Person1=Person()
Person1.setName('Ram')
print(Person1)
# print(Person1.getName())
# class Employee(Person):
#     emp_no=0
#     def getEmpNo(self):
#         return self.emp_no
#     def setEmpNo(self, new_num):
#         self.emp_no= new_num
#     def getName(self):
#         return 'Dr.' + Person.getName(self)
# E= Employee()
# E.setName("John")
# print(E.getName())
# E.setEmpNo(32)
# print(E.getEmpNo())
        

