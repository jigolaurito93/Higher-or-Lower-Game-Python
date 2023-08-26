from art import logo, vs
from game_data import data
import random

# Set score to zero for starting game
score = 0
# Turn flag to False to loop game until game ends and flag turn to True
game_over = False




# Start game here
while not game_over:
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
        account_followers = account['follower_count']
        return f"{account_name}, a {account_desc}, from {account_country}. {account_followers}"
    

    # Print Logo
    print(logo)

    # Compare account A
    print(f"Compare A: {format_data(account_a)}")
    # Print Vs Logo
    print(vs)
    # Compare account B
    print(f"Against B: {format_data(account_b)}")

    # Create an input to ask for the answer
    answer = input(f"Who has more followers? Type 'A' or 'B': ").upper()

    # Create an if statement to compare the number of followers and decide whether to quit the game or continue
    if account_a["follower_count"] > account_b["follower_count"]:
        if answer == "A":
            score += 1
        elif answer == "B":
            game_over = True
    elif account_a["follower_count"] < account_b["follower_count"]:
        if answer == "A":
            game_over = True
        elif answer == "B":
            score += 1








# when game is over, print logo and final score
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")