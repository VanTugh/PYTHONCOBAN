class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
    def displayStudent(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Lớp: {self.section}"
if __name__ == "__main__":
    st1 = Student("An", 20, "CBA1")
    print(st1.displayStudent())