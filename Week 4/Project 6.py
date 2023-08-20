"""
1. Define the function
2. Perform the calculations and return
3. prompt the user for input
4. call the function
5. print the results
"""

# Define the function for Leibniz approximation of pi
def leibniz_approx(num_iterations):
    approx = 0
    si = 1

    # Perform the approximation calculation
    for i in range(num_iterations):
        term = si / (2 * i + 1)
        approx += term
        si *= -1

    # Multiply the approximation by 4 to get pi
    pi_approx = 4 * approx

    # Return the calculated approximation
    return pi_approx

# Prompt the user for the number of iterations
num_iterations = int(input("Enter the number of iterations for the Leibniz approximation: "))

# Call the approx function and store the result
approx_result = leibniz_approx(num_iterations)

# Print the result
print("The approximation of pi using", num_iterations, "iterations is:", approx_result)
