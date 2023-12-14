class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year, born):
    super().__init__(fname, lname)
    self.graduationyear = year
    self.graduationyear1 = born

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, " to this world in", self.graduationyear , "my good frinde and " )

  def frinde(self):
    print("my frinde is :" , self.firstname , self.lastname , "and we met in :" , self.graduationyear1)

x = Student("mrs. sohrab", "khatar", 1381, 1402)
x.welcome()
x.frinde()