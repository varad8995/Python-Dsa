class Employee:
    def __init__(self) -> None:
        self.name = input("Enter your Name: ")
        self.age = int(input("Enter your Age: "))
        self.gender = input("Enter your Gender: ")
        self.phone_number = int(input("Enter your Phone Number: "))
    def calculate_monthly_salary(self):
        self.hourly_rate = int(input("Enter your hourly rate: "))
        self.hourly_worked = int(input("Enter your hour you worked in a year: "))
        return self.hourly_rate * self.hourly_worked
    def calculate_yearly_salary(self):
        return self.calculate_monthly_salary() * 12

employee1 = Employee()
print(
    f"employee monthly salry is {employee1.calculate_monthly_salary()} and yearly salary is {employee1.calculate_yearly_salary()}"
)