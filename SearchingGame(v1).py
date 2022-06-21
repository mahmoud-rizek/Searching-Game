userName = input("SuperMan: What is your name? ")
print(f"User: my name is {userName.title()}")
print(f"SuperMan: welcome {userName.title()} in our street, what are you doing here? ")

print(f"{userName.title()}: I looking for  someone")
userInput = input("SuperMan: looking for who? ")

buddies = ["pikachu" , "zimaa" , "grandizer" , "subzero" , "winner" , "tino" , "tico"]

for buddy in range(len(buddies)):
    if buddies[buddy] == userInput:
        print(f"SuperMan: {userInput.upper()} in {buddy + 1}")

    else:
        print(" ***** is here")
        

print(f"{userName.title()}: YES, found him! Thank you SuperMan")

