a, b, n = 1, 1, 2
A = int(input())

while a < A:
    a, b = b, a + b
    n += 1

if a == A:
    print(n)
else:
    print(-1)