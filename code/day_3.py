from math import pi, sqrt
age = 23
height = 1.8
complex_number = complex(5, 3)

base = int(input("Triangle Base: "))
height = int(input("Triange Base: "))
print("Triange Area: " + str(base * height * 0.5))

side_a = int(input("Side A: "))
side_b = int(input("Side B: "))
side_c = int(input("Side C: "))
print("Triange Perimeter: " + str(side_a + side_b + side_c))

radius = int(input("Circle perimeter: "))
area = pi * (radius ** 2)
print("Circle Area: " + str(area))
circumference = 2 * pi * radius

# y = mx + c
# y = 2x - 2
m = 2
c = -2

y_intercept = 2*0 - 2
x_intercept = 0 + 2 / 2
print("Y intercept: " + str(y_intercept))
print("X intercept: " + str(x_intercept))

x1, y1 = 2, 2
x2, y2 = 6, 10

# gradient
gradient = y2 - y1 / x2 - x1
print("Gradient: " + str(gradient))

euclidean_distance = sqrt(
    ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
)

print(m == gradient)

for x in range(-2, 6):
    y = x**2 + 6*x + 9
    print("x**2 + 6*x + 9")
    print(f"x={x}, y={y}")
     
length_1 = len("python")
length_2 = len("dragon")
print(length_1 != length_2)

print(
    ("on" in "python") and
    ("on" in "dragon")
)

print("jargon" in "I hope this course is not full of jargon")

print(type(10) == type("10"))
print(int(float("9.8")) == 10)

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
print("Your weekly earning is " + str(rate * hours))

years = int(input("Number of years lived: "))
print("You have lived for " + str(years * 365 * 24 * 60) + " seconds")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
