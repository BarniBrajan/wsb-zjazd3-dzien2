def print_more(required1, required2, *args):
    print("Parametr 1: ", required1)
    print("Parametr 2: ", required2)
    print("Everything else: ", args)


print_more(22,43,545234,"hehe","bleble",23123)