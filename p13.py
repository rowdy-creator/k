class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def display(self):
        print(f"{self.real}+{self.imag}i")
def add_two_complex(c1,c2):
    new_real=c1.real+c2.real
    new_imag=c1.imag+c2.imag
    return complex(new_real,new_imag)
n=int(input("enter no. of complex numbers: "))
result=complex(0,0)
for i in range(n):
    real=int(input("real part: "))
    imag=int(input("imag part: "))
    c=complex(real,imag)
    result=add_two_complex( result, c)

print("sum=",end="")

result.display()

