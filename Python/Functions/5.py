def kolor(kolor):
    if kolor == "czerwony":
        return "W tym kolorze mam jablka"
    elif kolor == "zielony":
        return "W tym  kolorze mam papryke"
    elif kolor == "zolty":
        return "W tym kolorze mam banana"
    else:
        return "Nie mam nic w tym kolorze"


print(kolor(input("Podaj kolor: ")))