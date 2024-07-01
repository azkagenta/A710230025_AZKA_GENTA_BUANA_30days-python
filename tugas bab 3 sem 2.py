class Employee:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__salary = 0.0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Buat object Employee
emp = Employee()

# Menggunakan method set untuk mengisi nilai atribut
emp.set_name("John Doe")
emp.set_age(30)
emp.set_salary(5000.0)

# Menggunakan method get untuk mengakses nilai atribut
print("Name:", emp.get_name())
print("Age:", emp.get_age())
print("Salary:", emp.get_salary())