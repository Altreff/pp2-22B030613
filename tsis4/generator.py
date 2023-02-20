
#1
def gensquares(N):
    for i in range(N):
        yield i**2

n = int(input())
for x in gensquares(n):
    print(x)

#2
def geneven(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in geneven(n):
    values.append(str(i))

print (",".join(values))
#3
def divthrfo(N):
    for i in range(N):
        if i!=0 and i%3 == 0 and i%4 == 0:
            yield i

n = int(input())
for x in divthrfo(n):
    print(x)

#4
def gensquaresrange(a,b):
    for i in range(a,b):
        yield i**2

a = int(input())
b = int(input())
for x in gensquaresrange(a,b):
    print(x)

#5
def fromntoo(N):
    for i in range(N, -1, -1):
        yield i

n = int(input())
for x in fromntoo(n):
    print(x)