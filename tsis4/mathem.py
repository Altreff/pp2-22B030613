#1
d = int(input())
drad = d * 3.14 / 180
print(f'In radians: {drad}')
#2
h = int(input())
a = int(input())
b = int(input())
print(f'Area of trapezoid is {(a+b)/2 * h}')
#3
import math

n = int(input())
s = int(input())
area = (n * s**2) / (4 * math.tan(math.pi/n))

print(f'The area is:{area}')

#4
a = int(input())
h = int(input())
print(f'Area of parallelogram: {a*h}')