def menu(wine, entree, desert="pudding"):
    return {"wine": wine, "enttree": entree, "desert": desert}

print(menu(wine="merlot",entree="chicken",desert="cake"))
print(menu(wine="merlot",entree="chicken"))