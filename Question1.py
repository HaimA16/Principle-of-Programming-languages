def factors_sum(n):
    x = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            x += i
            while n % i == 0:
                n //= i
        else:
            i += 1
    if n > 1:
        x += n
    return x if x > 1 else 0

number = int(input("Enter a number: \n"))
print(factors_sum(number))