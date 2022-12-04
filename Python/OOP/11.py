class Cat():
    
    def __init__(self, age, name):
        self.age = age
        self.name = name
        
        pass

    def print_text(self):
        print("Moj kot ma na imie %s i ma %s lat." % ( self.name, self.age ) )


kot1 = Cat(5,"Gustaw")
kot1.print_text()
