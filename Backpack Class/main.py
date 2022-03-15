#Create Class
class Backpack:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    #Open Bag
    def openBag(self):
        self.open = True
        print("This bag is now open")
    #Close bag
    def closeBag(self):
        self.open = False
        print("This bag is now closed")
    #Put in item 
    def putin(self, item):
        self.items.append(item)
        print("Your " + item + " has been added to your bag")
    #Take out item
    def takeout(self, item):
        if item in self.items:
            self.items.remove(item)
            print("You are now taking out your " + item)
        else:
            print(item + " is not in your bag")
#Create bags
bag1 = Backpack("blue", "small")
bag2 = Backpack("red", "medium")
bag3 = Backpack("green", "large")
#Command bag 
bag3.openBag()
bag3.putin("jacket")
bag3.putin("lunch")
bag3.closeBag()
bag3.openBag()
bag3.takeout("jacket")
bag3.closeBag()
