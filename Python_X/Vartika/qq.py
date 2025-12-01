class Fraction1: 
    def __init__(self,x, y):
        self.numurator  =x
        self.denominator =y
        print(x)
    def __str__(self): # string fucntion just to show how it will show 
        return '{}/{}'.format(self.numurator , self.denominator)
    def __add__(self,other):
        new_num = self.numurator*other.denominator + other.numurator*self.denominator
        new_den = self.denominator*other.denominator
        return '{}/{}'.format(new_num,new_den)
fr1 = Fraction1(3,4)
fr2 = Fraction1(3,5)
print(fr1+fr2)