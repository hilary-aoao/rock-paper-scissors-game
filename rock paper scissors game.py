import random
print("WELCOME TO THIS ROCK, PAPER, SCISSORS GAME!!!")
print("r is for rock")
print("p is for paper")
print("s is for scissors")
while True:
  user_action = input("Enter a choice (r, p, s): ").lower()
  possible_actions = ["r", "p", "s"]
  computer_action = random.choice(possible_actions)
  while user_action not in possible_actions:
      print("That's an error!!!")
      user_action = input("Enter another choice (r, p, s): ")
  print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

  if user_action == computer_action:
      print(f"Both players selected {user_action}. It's a tie!")
  elif user_action == "r":
      if computer_action == "s":
          print("R smashes s! You win!")
      else:
          print("P covers r! You lose.")
  elif user_action == "p":
      if computer_action == "r":
          print("P covers r! You win!")
      else:
          print("S cuts p! You lose.")
  elif user_action == "s":
      if computer_action == "paper":
          print("S cuts p! You win!")
      else:
          print("R smashes s! You lose.")
  play_again = input("Do you want to play again? (yes/no): ").lower()

  if play_again != "yes":
     
      break
print("See you later")   