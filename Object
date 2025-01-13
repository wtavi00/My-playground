import matplotlib.pyplot as plt

# Creating  class to draw the circle object
class Circle(object):
    # Main function of class circle
    def __init__(self,radius=5,color="green"):
        self.radius=radius # give the redius value to the self portion
        self.color=color   # give the color to the self portion
    # Add object radius to main function
    def add_radius(self,r):
        self.radius=self.radius+r
        return self.radius
    # Drow the circle
    def drowCircle(self):
        plt.gca().add_patch(plt.Circle((0,0),radius=self.radius,fc=self.color))
        plt.axis("scaled")
        plt.show()
GreenCircle=Circle(20,"green")
GreenCircle.drowCircle()

class Rectangle(object):
    # Main function of calss rectangle
    def __init__(self,height=5,width=3,color="green"):
        self.height=height
        self.width=width
        self.color=color
    # Add object height to main function
    def add_height(self,h):
        self.height=self.height+h
        return self.height
    # Add object width to main function
    def add_width(self,w):
        self.width=self.width+w
        return self.width
    # Droe the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0),self.width,self.height,fc=self.color))
        plt.axis("scaled")
        plt.show()
rect = Rectangle(height=4, width=6, color="green")
#rect.drowRectangle()


class Customer:
#We can put a lock on that data by adding a double underscore in front of it, as shown in below code.
# Adding a double underscore makes the attribute a private attribute. Private attributes are those which are accessible only inside the class. This method of restricting access to our data is called encapsulation.

    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)
