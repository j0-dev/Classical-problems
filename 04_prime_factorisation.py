def prime_factors(n):
    p_factors = []
    d = 2

    while n > 1:
        while n % d == 0:
            p_factors.append(d)
            n //= d
        d = d + 1

    return p_factors

print(prime_factors(540))

