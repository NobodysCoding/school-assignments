side1 = float(input("Enter the length for the first side: "))
side2 = float(input("Enter the length for the second side: "))
side3 = float(input("Enter the length for the third side: "))
 
# Sort the sides so that we can check if the largest side (hypotenuse) squared
# equals the sum of the squares of the other two sides
sides = sorted([side1, side2, side3])

# Check if the triangle is a right triangle
if sides[2] == sides[0] + sides[1]:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
