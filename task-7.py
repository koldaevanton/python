

def fact(num):
    for r in range(1, num + 1):
        f = 1
        for i in range(1, r + 1):
            f *= i
        yield f


n = 5

for el in fact(n):
    print(el)
