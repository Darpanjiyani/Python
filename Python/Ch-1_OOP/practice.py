class job():

    def __init__(self, title, salary):
        self.title = title
        self.salary = salary
    
    def answer(self):
        return f"{self.title} earns {self.salary} dollars per year."
    
object1 = job("Software Engineer", 100000)

print(object1.answer())