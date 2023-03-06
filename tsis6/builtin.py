#1
import math
l = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    el = int(input())
    l.append((el))

print(math.prod(l))

#2
a = input()
low = 0
up = 0
for i in a:
    if(i.islower()):
        low+=1
    else:
        up+=1

print("The number of lower:",low)
print("The number of upper:",up)

#3
if(a.lower() == ''.join(reversed(a)).lower()):
    print("Yes")
else:
    print("No")

#4
from time import sleep
b = int(input("Enter the number: "))
t = int(input("Enter time in ms: "))
sleep(t/1000)
print(f'The square root of {b} after {t}ms is: {math.sqrt(b)} ')


#5
tp = (True, False, True)
tp2 = (True, True, True)
print("Is tp1 has all elements true?: ", all(tp))
print("Is tp2 has all elements true?: ", all(tp2))
