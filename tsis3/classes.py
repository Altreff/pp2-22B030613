#1
class String():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = String()
str1.get_String()
str1.print_String()

#2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length
b = Square(0)
print(b.area())
a = int(input())
b = Square(a)
print (b.area())

#3
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width
d = int(input())
e = int(input())
r = Rectangle(d,e)
print(r.area())

#4
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"Point({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5


a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
p1 = Point(a1,b1)
p2 = Point(a2,b2)
print(p1.show())
m1 = int(input())
m2 = int(input())
p1.move(m1,m2)
print(p1.dist(p2))

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

nm = str(input())
mn = int(input())
acc = Account(nm, mn)
E = False
while(E!=True):
    print (f"{acc.owner}, what would you like to do?")
    print("B=Check balance   D=Deposit    W=Withdrawal   E=Exit")
    ans = str(input())
    if(ans == "D"):
        print("How much would you like to deposit?")
        dep = int(input())
        acc.deposit(dep)
    elif(ans == "B"):
        print(f"Current balance is: {acc.balance}$")
    elif(ans == "W"):
        print("How much would you like to withdraw?")
        wit = int(input())
        acc.withdraw(wit)
    elif(ans == "E"):
        print("Have a nice day!")
        E = True


#6
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

