class myClass:
    def myElement(self):
        print("This is parent class.")

class myChild(myClass):
    pass

obj = myChild()
obj.myElement()