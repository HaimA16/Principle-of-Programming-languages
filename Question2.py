def f(x):
    x = abs(x)
    return x + 1

def only_positive(f):
    def wrapper(x):
        result = f(x)
        return result
    return wrapper

g = only_positive(f)
number = float(input("enter number: \n"))
print(g(number))