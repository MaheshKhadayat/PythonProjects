import random

Game = ["Rock", "Paper", "Scissors"]  
while True:  
    User_Choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    
    if User_Choice not in Game:
        print("Invalid choice, try again!")
        continue 

    Computer_Choice = random.choice(Game)  
    print(f"Computer chose: {Computer_Choice}")

   
    if User_Choice == Computer_Choice:
        print("It is a tie breaker")
    elif (User_Choice == "Rock" and Computer_Choice == "Scissors") or \
         (User_Choice == "Paper" and Computer_Choice == "Rock") or \
         (User_Choice == "Scissors" and Computer_Choice == "Paper"):
        print("You won!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break  
