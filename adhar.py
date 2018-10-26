class adhar():
    """for adhar card"""
    def __init__(self,name,age,place,a_number,gen):
        self.name=name
        self.age=age
        self.place=place
        self.a_number=a_number
        self.gen=gen
    def display(self):
        """display function for adhar card"""
        print(self.name)
        print(self.age)
        print(self.place)
        print(self.a_number)
        print(self.gen)
class villager(adhar):
    """for village people"""
    def __init__(self,name,age,a_number,gen,village,city):
        adhar__init__(self,name,age,place,a_number,gen)
        super().display()
        self.village=village
        self.city=city
    def dis(self):
        """display function for village people"""
        print(self.village)
        print(self.city)
print(adhar.__doc__)
a1=adhar("komala",21,"tumkur",567890,"female")
print(adhar.display.__doc__)
a1.display()
print(villager.__doc__)
v1=villager("sudarshan",21,234567,"male","aynoor","shimoga")
print(villager.disp.__doc__)
v1.disp()
print(a1.__dict__)
print(v1.__dict__)
