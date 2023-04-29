import math

class Book:

    def __init__(self, no, l, d):
        self.no = no
        self.l = l
        self.d = d
    
    def __lt__(self, o):
        return self.l/self.d <= o.l/o.d

    def __str__(self):
        return str([self.no, self.l, self.d])

class B(Book):
    def __lt__(self, o):
        return self.d <= o.d


n, m = input().split()

n = int(n)
m = int(m)

books = []

for i in range(n):
    l, d = input().split()
    books.append(Book(i, int(l), int(d)))

books.sort()
books = books[:n-m]

bs = []
for b in books:
    bs.append(B(b.no, b.l, b.d))
bs.sort()

# lower = 0
# x0 = x = 10**4/2
# upper = 10**4
# while 1:
#     x0 = x
#     p = 0
#     for b in books:
#         p += b.l
#         if b.d * x < p:
#             lower = x
            
#         else:
#             upper = x
#         x = int((upper+lower)/2)
#     if x == x0:
#         break

x = 0
p = 0
for b in bs:
    p += b.l
    x = max(x, p/b.d)

print(math.ceil(x))
        


            