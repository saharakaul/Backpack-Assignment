class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    def openBag(self):
        self.open = True
        print("This bag is now open")
    def closeBag(self):
        self.open = False
        print("This bag is now closed")
    def putin(self, item):
        self.items.append(item)
        print("Your " + item + " has been added to your bag")
    def takeout(self, item):
        if item in self.items:
            self.items.remove(item)
            print("You are now taking out your " + item)
        else:
            print(item + " is not in your bag")

bag1 = Backpack("blue", "small")
bag2 = Backpack("red", "medium")
bag3 = Backpack("green", "large")

bag3.openBag()
bag3.putin("jacket")
bag3.putin("lunch")
bag3.closeBag()
bag3.openBag()
bag3.takeout("jacket")
bag3.closeBag()