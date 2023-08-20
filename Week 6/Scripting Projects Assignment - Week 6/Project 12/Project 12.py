def calculate_wages(hourly_wage, hours_worked):
    return hourly_wage * hours_worked

def print_payroll_report(file_name):
    try:
        with open(file_name, 'r') as file:
            print("Payroll Report")
            print("{:<15} {:<12} {:<12}".format("Employee Name", "Hours Worked", "Wages Paid"))
            print("-" * 43)

            for line in file:
                last_name, hourly_wage, hours_worked = line.strip().split()
                hourly_wage = float(hourly_wage)
                hours_worked = float(hours_worked)
                wages_paid = calculate_wages(hourly_wage, hours_worked)
                print("{:<15} {:<12.2f} ${:<12.2f}".format(last_name, hours_worked, wages_paid))
    except FileNotFoundError:
        print("File not found. Please check the file name and path.")

if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    print_payroll_report(file_name)
