import math
n=[]
k=int(input("enter the no of ele:"))
for i in range(k):
    v=int(input(f"enter the {i+1} ele : "))
    n.append(v)
mean=sum(n)/k
var=sum((x-mean)**2 for x in ngit)/k
std=math.sqrt(var)
print(mean)
print(var)
print(std)