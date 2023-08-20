"""
1. Prompt the user to enter the hourly wage.
2. Prompt the user to enter the total regular hours worked.
3. Prompt the user to enter the total overtime hours worked.
4. Call the calculate_weekly_pay function with the given inputs.
5. Print the employee's total weekly pay.
"""

# Function to calculate the employee's total weekly pay
def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
    regular_pay = hourly_wage * regular_hours
    overtime_pay = overtime_hours * 1.5 * hourly_wage
    total_pay = regular_pay + overtime_pay
    
    return total_pay

# Prompt the user to enter the hourly wage
hourly_wage = float(input("Enter the hourly wage: "))

# Prompt the user to enter the total regular hours worked
regular_hours = float(input("Enter the total regular hours worked: "))

# Prompt the user to enter the total overtime hours worked
overtime_hours = float(input("Enter the total overtime hours worked: "))

# Call the calculate function
total_weekly_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)

# Display the employee's total weekly pay
print("The employee's total weekly pay is:", total_weekly_pay)
