import math

def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break

    return estimate

def main():
    while True:
        # Receive the input number from the user
        try:
            x = input("Enter a positive number or press Enter to quit: ")
            if x == '':
                break
            x = float(x)
            if x < 0:
                print("Please enter a positive number.")
                continue
            estimate = newton(x)
            # Output the result
            print("The program's estimate:", estimate)
            print("Python's estimate      ", math.sqrt(x))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == '__main__':
    main()
