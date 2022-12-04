class CatParent():
    def voice(self):
        print("jestem rodzicem!")

class CatKid(CatParent):
  def voice(self):
    print("jestem dzieckiem!")
  def walk(self):
    print("Moge chodzic")

# print(issubclass(CatKid,CatParent))

parent = CatParent()
kid = CatKid()

parent.voice()
kid.voice()
kid.walk()