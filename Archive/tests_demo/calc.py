class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2 

    def get_sum(self):
        return self.num1 + self.num2
    
    #difference
    def difference(self):
        return self.num1 - self.num2
    #product
    def product(self):
        return self.num1 * self.num2
    #quotiant 
    def quotient(self):
        if self.num2 == 0:
            return 0
        return self.num1 / self.num2
    #stretch look into matrix dot product vs cross product
    
if __name__ == "__main__":
    myCalc = Calculator(144,12)
    print(myCalc.quotient())

    print(myCalc)