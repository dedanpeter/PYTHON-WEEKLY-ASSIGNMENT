class Student:
    # (i) Class named Student

    # (ii) Constructor to initialize name, registration number and course
    def __init__(self, name, reg_no, course):
        self.name = name
        self.reg_no = reg_no
        self.course = course

    # (iii) Method to display the student's information
    def display_details(self):
        print("Name:", self.name)
        print("Registration Number:", self.reg_no)
        print("Course:", self.course)
        print()


# (iv) Create two objects and call display_details() for each
student1 = Student("John Mwangi", "BSCIT-01-0001/2026", "Information Technology")
student2 = Student("Mary Achieng", "BSCIT-01-0002/2026", "Business Information Technology")

student1.display_details()
student2.display_details()
