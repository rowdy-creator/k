import os
p=os.walk("/home/kuro/python")
for c,d,f in p:
    print("cwd",c)
    for k in d:
        print("folder",k)
    for h in f:
        print("file",h)


