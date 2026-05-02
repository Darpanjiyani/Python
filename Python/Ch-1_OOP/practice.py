class morning:

    var1 = "Hello Everyone"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def gm(self):
        print("Good Morning!")

    def name(self):
        print(f"My name is {self.first_name} and yes, I do have my last name as well, it's {self.last_name}")
        
obj1 = morning("Darpan", "Jiyani")
print(obj1.var1)
obj1.gm()
obj1.name()
