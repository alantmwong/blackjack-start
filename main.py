############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from art import logo

# Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Create a function called calculate_score() that takes a List of cards as input
# and returns the score. 
  
def calculate_score(hand):
  """Takes a list of cards and returns the score"""
  score = sum(hand)
  # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 
  # instead of the actual score. 0 will represent a blackjack in our game. 
  if len(hand) == 2 and score == 21:
    return 0
  # Removing the 11 (Ace) inside a hand if the score is over 21 to become 
  # a value of 1
  if 11 in hand and score > 21:
    hand.remove(11)
    hand.append(1)
    score -= 10
    
  return score

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, 
# then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score
# is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with 
# the highest score wins.

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It is a draw."
  elif computer_score == 0:
    return "You lose. Computer has blackjack."
  elif user_score == 0:
    return "You win! You have blackjack."
  elif user_score > 21:
    return "You lose. Bust."
  elif computer_score > 21:
    return "You win! Computer bust."
  elif user_score > computer_score:
    return "You win! "
  else: 
    return "You lose. "
  
def play_blackjack():  
  # Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards = []
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  game_over = False
  while game_over == False:
    # The score will need to be rechecked with every new card drawn and the checks
    # need to be repeated until the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
      game_over = True
    # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else: 
      hit = input("Do you want to draw another card?: Type 'y' or 'n' \n")
      if hit == 'y':
        user_cards.append(deal_card())
      else: 
        game_over = True
    

  # Once the user is done, it's time to let the computer draw. The computer should keep drawing cards as long as it has 
  # a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of 
# blackjack and show the logo from art.py.

while (input("Do you want to play blackjack? Type 'y' or 'n' \n")) == 'y':
  print(logo)
  play_blackjack()



