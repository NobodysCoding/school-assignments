"""
1.get user input for starting salary and remove any commas
2.Convert string to float
3.get user input for percentage
4.initialize empty array
5.compute and store salary for each year
6.print the salary chedule in tabular format

"""


# Get user input for starting salary
starting_salary_str = input("Enter the starting salary for teachers: ")

starting_salary_str = starting_salary_str.replace(",", "")

starting_salary = float(starting_salary_str)

# Get user input for percentage increase and number of years
percentage_increase = float(input("Enter the percentage increase per year: "))
num_years = int(input("Enter the number of years in the salary schedule: "))

# Initialize an empty list to store the salary schedule
salary_schedule = []

# Calculate and store the salary for each year in the schedule
for year in range(1, num_years + 1):
    salary = starting_salary * (1 + percentage_increase / 100) ** (year - 1)
    salary_schedule.append((year, salary))

# Print the salary schedule in tabular format
print("Salary Schedule:")
print("Year      Salary")
for year, salary in salary_schedule:
    print(f"{year:<10d} {salary:<10.2f}")
