class Employee:
    # (i) Class named Employee with attributes employee_id, name, basic_salary, overtime_hours
    # (ii) Constructor to initialize the four attributes
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    # (iii) Gross Salary = Basic Salary + (Overtime Hours * 500)
    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    # (v) Tax = 10% of the gross salary
    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

    # (iv) Net Salary = Gross Salary - (Gross Salary * 0.10)
    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        return gross_salary - (gross_salary * 0.10)


# (vi) Create two employee objects and display gross salary, tax and net salary
employee1 = Employee("EMP101", "Alice", 50000, 10)
employee2 = Employee("EMP102", "Brian", 65000, 6)

print("Employee ID:", employee1.employee_id)
print("Name:", employee1.name)
print("Gross Salary: KSh", employee1.calculate_gross_salary())
print("Tax: KSh", employee1.calculate_tax())
print("Net Salary: KSh", employee1.calculate_net_salary())
print()

print("Employee ID:", employee2.employee_id)
print("Name:", employee2.name)
print("Gross Salary: KSh", employee2.calculate_gross_salary())
print("Tax: KSh", employee2.calculate_tax())
print("Net Salary: KSh", employee2.calculate_net_salary())
