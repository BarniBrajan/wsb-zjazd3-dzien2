class Czlowiek():
  def __init__(self, name):
    self._name = name

class EmailCzlowiek(Czlowiek):
  def __init__(self, name, email):
    super().__init__(name)
    self.email = email

  def printName(self):
    print(self._name)



cz = EmailCzlowiek("Imie Nazwisko", "imie@nazwisko.com")
cz.printName()

