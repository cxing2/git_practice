class Calculator():
    def add(self, num1, num2):
        #return num1 + num2
        return 2
    def substract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return 0
if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(1, 2))
    print(calculator.substract(1, 2))
    print(calculator.multiply(1, 2))
    print(calculator.divide(1, 2))
        
