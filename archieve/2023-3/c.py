import math

class Book:

    def __init__(self, no, l, d):
        self.no = no
        self.l = l
        self.d = d

    def include(self, books):
        for b in books:
            if b.no == self.no:
                return True
        return False
    
    def __lt__(self, o):
        return self.d <= o.d


class B(Book):
    def __lt__(self, o):
        return self.l/self.d <= o.l/o.d
    

n, m = map(int, input().split())

books = []

for i in range(n):
    l, d = map(int, input().split())
    books.append(Book(i, l, d))
books.sort()

p = 0
bs = []
for b in books:
    p += b.l
    bs.append(B(b.no, p, b.d))
bs.sort()
bs = bs[n-m:]

x = p = 0
for b in filter(lambda b: b.include(bs), books):
    p += b.l
    x = max(x, p/b.d)

print(math.ceil(x))

