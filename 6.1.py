print("LE TUAN ANH")
print("MSSV: 235752021610050")
class Circle(object):
    def __init__(self, r):
       self.radius = r
    def area(self):
       return self.radius**2*3.14
aCircle = Circle(2)
print (aCircle.area())
