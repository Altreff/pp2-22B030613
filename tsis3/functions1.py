#1
def ounces(m):
    return 28.3495231 * m
m = float(input())
print(ounces(m))

#2
def cel(f):
    return (5/9)*(f-32)
f=int(input())
print(cel(f))

#3
def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    if (heads >= legs):
        print(error_msg)
    elif (legs % 2 != 0):
        print(error_msg)
    else:
        rabbit_count = (legs - 2 * heads) / 2
        chicken_count = heads - rabbit_count
        print(int(chicken_count), int(rabbit_count))

h = int(input())
l = int(input())
solve(h,l)

#4

def is_prime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if(n%i) == 0:
            return False
        return True

lst = []


n = int(input("Enter number of elements : "))

for i in range(0, n):
    el = int(input())

    lst.append(el)
for i in range(1, 10):
    prime_lst = list(filter(lambda x: (is_prime(x) == True), lst))
print(prime_lst)

#5

def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


str = str(input())
n = len(str)
a = list(str)

permute(a, 0, n)

#6

def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end -= 1


s = input()

s = list(s)
start = 0
while True:

       try:
        end = s.index(' ', start)

        reverse_word(s, start, end - 1)

        start = end + 1

       except ValueError:
            reverse_word(s, start, len(s) - 1)
            break

s.reverse()

s = "".join(s)

print(s)

#7

def has_33(x):
    for i in range(0, len(x)-1):
        if x[i:i+2] == [3, 3]:
            print("True")
            return True
    print("False")
    return False

ls = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    el = int(input())

    ls.append(el)

has_33(ls)

#8
def has_007(x):
    for i in range(0, len(x)-2):
        if x[i] == 0 and x[i+1] == 0 and x[i+2]==7:
            print("True")
            return True
    print("False")
    return False

le = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    el = int(input())

    le.append(el)

has_007(le)

#9
def vol(x):
    return (4/3)*3.14*(x**3)

r = int(input())
print(vol(r))

#10
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

u=[]
n = int(input("Enter number of elements : "))

for i in range(0, n):
    el = int(input())

    u.append(el)

print(unique_list(u))

#11
def is_palindrome(s):
    return s == s[::-1]

w = input()
if is_palindrome(w):
    print("Palindrome")
else:
    print("Not")

#12
def histogram(q):
    for i in range(len(q)):
        print(q[i]*'*')

q = []
n = int(input("Enter number of lines: "))

for i in range(0, n):
    el = int(input())
    q.append(el)
histogram(q)

#13
import random

print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20")
r1 = random.randint(1, 20)
answer = int(200)
guess = 1
while answer != r1:
    print("Take a guess")

    answer =  int(input())
    if answer > r1:
        print("Your guess is too high.")
        guess += 1
    elif answer < r1:
        print("Your guess is too low.")
        guess += 1
    elif answer == r1:
        print(f"Good job, {name}! You guessed my number in {guess} guesses!")
