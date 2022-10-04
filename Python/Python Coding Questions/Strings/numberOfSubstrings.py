class MyClass:
    def __init__(self, str1):
        self.str1 = str1
    
    def subString(self):
        ls = []
        for i in range(len(self.str1)):
            s = self.str1[i]
            ls.append(s)
            for j in range(i + 1, len(self.str1)):
                s = s + self.str1[j]
                ls.append(s)
        print(len(ls))


obj = MyClass("abcd")
obj.subString()