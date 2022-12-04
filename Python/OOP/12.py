class CatParent():
    def voice(self):
        print("jestem rodzicem!")

class CatKid(CatParent):
  pass


# print(issubclass(CatKid,CatParent))

parent = CatParent()
kid = CatKid()

parent.voice()
kid.voice()