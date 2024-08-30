import random

print("Welcome to Rock Paper Scissor Game!")

while True:
  try:
    print("Enter your choice: 1 for Scissors ,2 for Paper and 3 for Rock.")
    user_choice = int(input("Enter your choice : "))
    user_options = [1, 2, 3]

    if user_choice not in user_options:
      ValueError("Your choice is invalid! Kindly input a valid choice!")
      continue
    computer_choice = random.choice(user_options)

    if user_choice == 1:
      if computer_choice == 2:
        print(f"Bot choosed:{computer_choice}")
        print("You win!")
      elif computer_choice == 3:
        print(f"Bot choosed:{computer_choice}")
        print("You lose")
      elif computer_choice == 1:
        print(f"Bot choosed:{computer_choice}")
        print("It is a draw!")

    if user_choice == 2:
      if computer_choice == 1:
        print(f"Bot choosed:{computer_choice}")
        print("You lose!")
      elif computer_choice == 3:
        print(f"Bot choosed:{computer_choice}")
        print("You Win")
      elif computer_choice == 2:
        print(f"Bot choosed:{computer_choice}")
        print("It is a draw!")

    if user_choice == 3:
      if computer_choice == 1:
        print(f"Bot choosed:{computer_choice}")
        print("You Win!")
      elif computer_choice == 3:
        print(f"Bot choosed:{computer_choice}")
        print("It is a draw!")
      elif computer_choice == 2:
        print(f"Bot choosed:{computer_choice}")
        print("You lose!")

    play_again = input('Do you want to play again? (yes/no):')

    if play_again.lower() != 'yes':
      break

  except:
    print("Invalid value. Please Enter 1, 2, 3.")

print("Thanks for playing.!")
