def read_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        numbers = [float(line.strip()) for line in lines]
        return numbers

def compute_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count > 0:
        average = total / count
        return average
    else:
        return 0

def main():
    filename = 'numbers.txt'
    numbers = read_numbers(filename)
    average = compute_average(numbers)
    print(f"The average of the numbers is: {average:.2f}")

if __name__ == "__main__":
    main()
