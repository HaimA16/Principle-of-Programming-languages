def print_numbers(first, last, num):
    if first < last:
        if first != num:
            print(first)
        print_numbers(first + 1, last, num)
    elif last < first:
        print_numbers(first, last + 1, num)
        if last != num:
            print(last)
    elif first == last and first != num:
        print(first)

first = int(input("Enter first number: \n"))
last = int(input("Enter last number: \n"))
num = int(input("enter number: \n"))
print_numbers(first, last, num)