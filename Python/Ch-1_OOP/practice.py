class sabha:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def fun(self):
        return f"My name is {self.name} and I am {self.age} years old."

obj = sabha("Darpan", 24)
print(obj.fun())