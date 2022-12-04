class Zwierze():
  def glos(self):
    return "Ja mowie!"

class Malpa(Zwierze):
  def glos(self):
    return "uhuhaha"

class Kon(Zwierze):
  def glos(self):
    return "ihahaha"

class Pies(Malpa, Kon):
  pass

class Kot(Kon, Malpa,):
  pass


# print(Pies.mro())

pi = Pies()
print(pi.glos())
