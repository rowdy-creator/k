
import csv
with open("data.csv","r")as f:
    data=list(csv.DictReader(f))
print("column:", list(data[0].keys()))
col=input("enter column name:")
nums=[]
for row in data:
    try:
        nums.append(float(row[col]))
    except:
        pass
op=input("type max/min/avg:")
if op=='max':
    print("max:", max(nums))
elif op=='min':
    print("min:", min(nums))
elif op=='avg':
    print("avg:", sum(nums)/len(nums))