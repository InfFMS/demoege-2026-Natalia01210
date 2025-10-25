def F(N):
    R = ''
    n = N
    while n > 0:
        R = R + str(n%2)
        n //= 2
    R = R[::-1]
    if N % 3 == 0:
        R = R + R[len(R)-3:len(R)]
    else:
        r = N % 3
        r *= 3
        q = ''
        Q = r
        while Q > 0:
            q = q + str(Q % 2)
            Q //= 2
        q = q[::-1]
        R = R + q
    s = 0
    i = 0
    R = int(R)
    while (R > 0):
        s += (R % 10) * 2 ** i
        i += 1
        R //= 10
    return s

for i in range(4, 100):
    if (F(i) >= 200):
        print(i)
        break

print(3 **8)