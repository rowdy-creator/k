with open("/home/kuro/python/final/5.txt") as f:
    l=f.readlines()
data=[x.strip() for x in l]

data.sort()
with open("o1.txt","w") as fi:
    for xi in data:
        fi.write(xi+"\n")
