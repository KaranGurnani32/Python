class Student:
    def __init__(self):
        self.first_name = "Karan"
        self.last_name = "Gurnani"
        self.id = 47
        self.standard = "12th"
        self.school = "Mount Abu School"
        self.friends = ["Kanishk", "Kunal", "Akkshay", "Indrankur", "Pragati"]

    def show_data(self):
        print("Name: " + self.first_name + " " + self.last_name + ",")

student1 = Student()
student1.show_data()