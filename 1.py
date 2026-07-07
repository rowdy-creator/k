a =int(input("enter a no"))
b =int(input("enter 2nd no"))
c =int(input("enter your choice"))
if c==1:
    print("add",a+b)
elif c==2:
    print("sub",a-b)
elif c==3:
    print("mult",a*b)
elif c==4:
    print("div",a/b)
else:
    print("invalid character")