from math import sqrt
import matplotlib.pyplot as plt
import numpy as np #to use 'arange','linspace' method


#class to which takes coefficients and calculates the roots
class qudratic_solver:
    def __init__(self,coefficent_of_x2:int,coefficent_of_x:int,contant_term:int) :
        self.a=coefficent_of_x2
        self.b=coefficent_of_x
        self.c=contant_term
        self.z=self.b*self.b-4*self.a*self.c
        self.root1,self.root2=0,0

    
    def cal_root(self):   #to calculate roots
        if self.z<0:
            print("Roots are Imaginary!")
            self.real=-self.b/(2*self.a)
            self.img=sqrt(-self.z)/(2*self.a)
            self.root1=complex(self.real,self.img)
            self.root2=complex(self.real,self.img)
        else:
            self.root1=(-self.b+sqrt(self.z))/(2*self.a)
            self.root2=(-self.b-sqrt(self.z))/(2*self.a)
        return self.root1,self.root2
    
    @property
    def is_real(self):         #to check if the roots are real or not
        if self.z<0:
            return False
        return True
    @property
    def x_for_min_y(self):
        return -self.b/(2*self.a)
    

    def get_value(self,x):    #to get the value of y at any x
        return self.a*x*x+self.b*x+self.c

    def __repr__(self) :
        return f"{self.a}x^2+{self.b}x+{self.c}"
    def __str__(self) :
        return f"roots: {self.root1} ; {self.root2}"


a,b,c=map(int,input("Enter The Value of a,b,c: ").split(",")) #takes the coefficient from user

# quad=qudratic_solver(1,-9,14)
quad=qudratic_solver(a,b,c) #creating object
quad.cal_root()
print(quad)

plt.figure(figsize=(10,7))   #size of frame


#to plot the solution of quadratic equation
if(quad.is_real):
    x_data=np.linspace(quad.root2-5,quad.root1+5,1000)
    # x_data=np.arange(quad.root2-5,quad.root1+5,0.001)
    plt.scatter(quad.root1,quad.get_value(quad.root1),c="red")
    plt.scatter(quad.root2,quad.get_value(quad.root2),c="red")
    plt.title("Curve of Quadratic Equation(Real Roots)") 

    
else:  
    # x_data=np.arange(quad.x_for_min_y-5,quad.x_for_min_y+5,0.001)
    x_data=np.linspace(quad.x_for_min_y-5,quad.x_for_min_y+5,1000)
    plt.title("Curve of Quadratic Equation (Imaginary Roots)")


#creating a dataset for y using x within a range
y_data=np.array([])
for i in x_data:   
    y_data=np.append(y_data,[quad.get_value(i)])
# print(x_data)
# print(y_data)

#ploting the curve of quadratic equation
plt.plot(x_data,y_data)
plt.plot([x_data[0],x_data[-1]],[0,0])   #to show a ref line (y=0)
plt.plot([0,0],[y_data[0],y_data[-1]])   #to show a ref line (x=0)

plt.xlabel("x ->")
plt.ylabel("y ->")
plt.grid(True)
plt.show()