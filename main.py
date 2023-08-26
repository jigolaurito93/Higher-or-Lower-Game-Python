from art import logo, vs
from game_data import data
import random

# Create a generator to generate a random account
account_a = random.choice(data)
account_b = random.choice(data)

# Create an if statement to check if accountA is similar to accountB, if yes, regenerate the account
if account_a == account_b:
    account_b = random.choice(data)

# Create a function that takes the account as an argument and format the data
def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    print(f"{account_name}, a {account_desc}, from {account_country}.")

format_data(account_a)

# print(person["name"])

# Print the message of the random profile
def print_messageA(person):
    pass







rand_int = random.randrange(len(data))

# Create a flag to indicate whether game is running or not
game_over = False

game_score = 0
# Create a while loop until game is finished
while not game_over:
    # Print Logo
    print(logo)
    # If has score, print score here
    if game_score > 0:
        print(game_score)
    # Show comparison A
    break
    # Print Vs
    # Show Comparison B

    # Who has more followers(input)








# when game is over, print logo and final score