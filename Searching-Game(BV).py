buddies = ["pikachu" , "zimaa" , "grandizer" , "subzero" , "winner" , "tino" , "tico"]

for buddy in range(len(buddies)):
    if buddies[buddy] == "tino":
        print(f"{buddy + 1}- tino is here")
    elif buddies[buddy] == "tico":
        print(f"{buddy + 1}- tico is here")
    elif buddies[buddy] == "zimaa":
        print(f"{buddy + 1}- zimaa is here")
    else:
        print(f"{buddy + 1}- no one here")
