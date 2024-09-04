import math
import matplotlib.pyplot as plt
import numpy as np



class polynomial_solver:
    def __init__(self,degree,coefficients):
        self.degree=degree
        self.coefficients=np.array(coefficients)
        self.roots=np.array(np.roots(self.coefficients))
    
    def get_value(self,x):    #to get the value of y at any x
        value=0
        for i in range(self.degree+1):
            value=value+(self.coefficients[i]*(x**(self.degree-i)))
        return value
    
    def real_roots(self):
        real=[]
        for i in self.roots:
            if i.imag==0:
                real.append(i.real)
        return real
    
    def imag_roots(self):
        imag=[]
        for i in self.roots:
            if i.imag!=0:
                imag.append(i)
        return imag
    
coefficients=[]
degree=int(input("Enter Degree of Polynomial: "))
for i in range(degree+1):
    coefficients.append(int(input("Coefficient: ")))
solv=polynomial_solver(degree,coefficients)


if len(solv.real_roots())!=0:
    x_data=np.linspace(min(solv.real_roots())-5,max(solv.real_roots())+5,100)
else:
    x_data=np.linspace(-1000,1000,1000)

y_data=np.array([])
for i in x_data:
    y_data=np.append(y_data,solv.get_value(i))

root_str="Roots are: "
for i in solv.roots:
    root_str=root_str+str(i)+" , "
print(root_str[:-2])


y_for_real_roots=[]
for i in solv.real_roots():
    y_for_real_roots.append(solv.get_value(i))

plt.scatter(solv.real_roots(),y_for_real_roots,c="red")
plt.plot(x_data,y_data)
plt.plot([x_data[0],x_data[-1]],[0,0])   #to show a ref line (y=0)
plt.xlabel("x ->")
plt.ylabel("y ->")
plt.grid(True)
plt.show()

