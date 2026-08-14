# Display art
from art import logo, vs
from game_data import data
print(logo)
import random

def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Generate a random account from game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# Ask user for a guess
guess = input("Who has more followers? A or B: ").lower()

# check if user is correct?
## get follower count of each follower
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]

## use if statement to check if user is correct

# give user feedback on their answer

# score keeping

# make the game repeatable

# making account of position B becomes position A at next round.


