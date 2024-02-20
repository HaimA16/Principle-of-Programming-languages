def list_product(list1,list2):
    j = 0
    y = 0
    list3 = []
    for k in list1:
        for i in range(list2[j]):
            list3.append(k)
            y += 1
        j += 1
    return list3

list1 = list(map(int, input("Enter numbers for list 1 separated by space: ").split()))
list2 = list(map(int, input("Enter numbers for list 2 separated by space: ").split()))
list3 = list_product(list1, list2)
print(list3)