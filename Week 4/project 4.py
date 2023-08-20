"""
1. define the function
2. perform calculations and return
3. get the user input
4. call the function and calculate
5. print the results.
"""

# Define the function to calculate the total distance traveled by the ball
def calculate_distance(initial_height, num_bounces, bounciness_index):
    distance = initial_height
    total_distance = initial_height

    # Perform the calculation for each bounce
    for _ in range(num_bounces):
        distance *= bounciness_index
        total_distance += 2 * distance

    # Return the total distance traveled
    return total_distance

# Prompt the user for input
initial_height = float(input("Enter the initial height of the ball (in feet): "))
num_bounces = int(input("Enter the number of times the ball is allowed to bounce: "))

# Validate and prompt the user for the bounciness index
while True:
    bounciness_index = float(input("Enter the bounciness index of the ball (between 0.1 and 0.9): "))
    if 0.1 <= bounciness_index <= 0.9:
        break
    else:
        print("Invalid input. Please enter a bounciness index between 0.1 and 0.9.")

# Call the function to calculate the total distance traveled by the ball
total_distance = calculate_distance(initial_height, num_bounces, bounciness_index)

# Print the result
print("The total distance traveled by the ball is:", total_distance, "feet")
