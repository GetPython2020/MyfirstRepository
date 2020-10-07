class Emp():
    def __init__(self, name):
        self.name = name
    def get_salary(self):
        pass

class Manager(Emp):
    def get_salary(self):
        return 15000

class Programmer(Emp):
    def __init__(self,name,hour):
        super().__init__(name)
        self.work_hour = hour
    def get_salary(self):
        return 150*self.work_hour
class Sales(Emp):
    def __init__(self,name,sales):
        super().__init__(name)
        self.sales = sales
    def get_salary(self):
        return 1200+0.05*self.sales

manage1 = Manager('Bob')
programmer1 = Programmer('Tom',80)
sale1 = Sales('Jane',20000)

print(f'{manage1.name}\'s salary is {manage1.get_salary()}')
print(f'{programmer1.name}\'s salary is {programmer1.get_salary()}')
print(f'{sale1.name}\'s salary is {sale1.get_salary()}')


