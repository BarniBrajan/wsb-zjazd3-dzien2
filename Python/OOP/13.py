class Czlowiek():
  def __init__(self, name):
    self.name = name

class Lekarz(Czlowiek):
  def __init__(self, name):
    super().__init__(name)
    self.proffesion = "Lekarz: %s" % self.name

class Prawnik(Czlowiek):
  def __init__(self, name):
    super().__init__(name)
    self.proffesion = "Prawnik: %s" % self.name


# lekarz = Lekarz("Janusz")
# prawnik = Prawnik("Tobiasz")
peopleList = []
peopleList.append(Lekarz("Janusz"))
peopleList.append(Prawnik("Tobiasz"))

for item in peopleList:
  print(item.proffesion)
