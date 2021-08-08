class AppleBasket:
    def __init__(self, initX, initY):
        self.apple_color = initX
        self.apple_quantity = initY
    def increase(self):
        return self.apple_quantity + 1
    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)    
testOne = AppleBasket('red',4)
print(testOne)
testOne.increase()
print(testOne)