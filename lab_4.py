class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        results = [employee for employee in self.employees if employee.age == target_age]
        return results

    def search_by_name(self, target_name):
        results = [employee for employee in self.employees if employee.name == target_name]
        return results

    def search_by_salary(self, operator, target_salary):
        if operator == ">":
            results = [employee for employee in self.employees if employee.salary > target_salary]
        elif operator == "<":
            results = [employee for employee in self.employees if employee.salary < target_salary]
        elif operator == ">=":
            results = [employee for employee in self.employees if employee.salary >= target_salary]
        elif operator == "<=":
            results = [employee for employee in self.employees if employee.salary <= target_salary]
        else:
            results = []
        return results

def main():
    database = EmployeeDatabase()
    
    # Add employee data to the database
    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Search Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        target_age = int(input("Enter the age to search: "))
        results = database.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter the name to search: ")
        results = database.search_by_name(target_name)
    elif choice == 3:
        operator = input("Enter the operator (>, <, <=, >=): ")
        target_salary = int(input("Enter the salary to search: "))
        results = database.search_by_salary(operator, target_salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("\nSearch Results:")
        for employee in results:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
    else:
        print("\nNo results found.")

if __name__ == "__main__":
    main()