# A simple OOP example
class Employee:
    # First i am initializing the parameters with the __init__ method, in this case it takes the earnings of in employee
    def __init__(self, earnings):
        self.earnings = earnings
    # This code takes the employees earnings and prints their job title
    def title(self):
        value = int(self.earnings)
        if value <= 50:
            print("Manager")
        elif value < 90:
            print("Lead Developer")
        else:
            print("Project manager")

# Here I am assigning three people with the employee object
john = Employee(70)
jack = Employee(40)
jill = Employee(150)

# Here I am calling the title method to print their job titles
john.title()
jack.title()
jill.title()