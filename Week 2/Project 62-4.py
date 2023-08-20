#define radius, diameter, cicumference, surface area, and volumn
#perform math operations
#print diameter, cicumference, surface area, and volumn

import math

radius = float(input("Enter the radius of the sphere: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius ** 2
volume = 4/3 * math.pi * radius ** 3

print("Diameter: " + str(diameter))
print("Circumference: " + str(circumference))
print("Surface Area: " + str(surface_area))
print("Volume: " + str(volume))
