n=input("enter a number")
for x in set(n):
    print(f"{x} is appeared {n.count(x)} times")