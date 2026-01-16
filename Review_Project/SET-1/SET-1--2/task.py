def get_employee_data():
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary_per_hour = float(input("Enter Salary Per Hour: "))

        print("Enter working hours for 7 days:")
        daily_hours = []
        for day in range(1, 8):
            hours = float(input(f"Day {day} hours: "))
            daily_hours.append(hours)

        return emp_id, name, salary_per_hour, daily_hours

    except ValueError:
        raise ValueError("Invalid input! Please enter numeric values for ID, salary, and hours.")


def calculate_wage(daily_hours, salary_per_hour):
    daily_wages = [hours * salary_per_hour for hours in daily_hours]
    total_hours = sum(daily_hours)
    total_wage = sum(daily_wages)

    if total_hours > 40:
        bonus = total_wage * 0.10
        total_wage += bonus
    else:
        bonus = 0

    return daily_wages, total_hours, bonus, total_wage


def save_to_file(employee_data):
    with open("C:\Users\dhira\Desktop\OOps\Review_Project\SET-1\SET-1--2\employee_records.txt", "a") as file:
        file.write(str(employee_data) + "\n")


employees = {}
highest_earner = None
max_salary = 0

try:
    n = int(input("Enter number of employees: "))

    for _ in range(n):
        emp_id, name, salary_per_hour, daily_hours = get_employee_data()
        daily_wages, total_hours, bonus, total_wage = calculate_wage(daily_hours, salary_per_hour)

        employees[emp_id] = {
            "Name": name,
            "Daily Hours": daily_hours,
            "Daily Wages": daily_wages,
            "Total Hours": total_hours,
            "Bonus": bonus,
            "Total Wage": total_wage
        }

        save_to_file(employees[emp_id])

        if total_wage > max_salary:
            max_salary = total_wage
            highest_earner = name

    print("\nEmployee Data:")
    for emp_id, details in employees.items():
        print(emp_id, details)

    print(f"\nHighest Earning Employee: {highest_earner} with ₹{max_salary}")

except Exception as e:
    print(e)
