def interceptPoint(line1, line2):
    a1, b1 = line1
    a2, b2 = line2

    if a1 == a2:
        return None

    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1

    return x, y

Line1 = tuple(map(float, input("Enter two numbers for line 1 separated by space: ").split()))
Line2 = tuple(map(float, input("Enter two numbers for line 2 separated by space: ").split()))

if interceptPoint(Line1, Line2):
    print(interceptPoint(Line1, Line2))
else:
    print("No intersection point.")