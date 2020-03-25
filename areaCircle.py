# AREA OF A CIRCLE
# This is a simple code for calculating the area of a circle, given the radius.

print ("Hey! I am Hunta, a nanobot.\nGive me the Radius of a Circle and I will magically give you it's Area\n") #Giving it an interactive feel

radius = input("Input your value: ") #Accept values
pi = 3.1429 #Assign 3.1429 to pi
X = float(radius) #Typecasting the user value (radius) to float

Area = pi * (X ** 2) #Formula for calculating Area of a Circle

print ("The Area of a Circle with radius " + radius + " is", Area) #Output result