import random 

computer = random.choice([1,2,3])

you=int(input("enter your number: "))

dic={1:"rock",
     2:"paper",
     3:"scissors"}

game=dic[you]  #if user enter 1 or 2 or 3 then it will choose from dic its value 
game2=dic[computer]#same with it if computer randomly gives 1 then it will print rock from dic and so on 


print(f"you choose {game}\n computer choose {game2}")

if(game==game2):
    print("its a draw")

elif (game == "rock" and game2 == "scissors") or \
     (game == "paper" and game2 == "rock") or \
     (game == "scissors" and game2 == "paper"):
    print("You won")

else:
    print("Computer won")

