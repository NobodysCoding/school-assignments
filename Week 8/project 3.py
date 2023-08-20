import math

def newton(x, estimate=1.0):
    # Initialize the tolerance
    tolerance = 0.000001

    # Check the estimate
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    while True:
        try:
            x = input("Enter a positive number or press Enter to quit: ")
            if x == '':
                break
            x = float(x)
            if x < 0:
                print("Please enter a positive number.")
                continue
            # calling the newton function without a second argument
            estimate = newton(x)
            # Output the result
            print("The program's estimate:", estimate)
            print("Python's estimate      ", math.sqrt(x))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == '__main__':
    main()
