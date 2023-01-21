# Import Module
from random import randint

# Create Deck of Cards
cards = []
symbols = ["♤", "♡", "♢", "♧"]
nums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for n in nums:
    for s in symbols:
        cards.append(n + s)

# Community cards (Flop, Turn, River)
community_list = []
while len(community_list) < 5:
    x = cards[randint(0, len(cards) - 1)]
    if x not in community_list:
        community_list.append(x)

community_string = " | ".join(community_list)

# Draw your Cards
player_1_hand = []
while len(player_1_hand) < 2:
    x = cards[randint(0, len(cards) - 1)]
    if (x not in player_1_hand) and (x not in community_list):
        player_1_hand.append(x)

player_1_string = " | ".join(player_1_hand)
player_1_situation = player_1_hand + community_list
situation_1_string = player_1_string + community_string

# Translate Symbols to numbers
numbers_list = []
for i in player_1_situation:
    if len(i) == 2:
        if i[0] == "J":
            numbers_list.append(11)
        elif i[0] == "Q":
            numbers_list.append(12)
        elif i[0] == "K":
            numbers_list.append(13)
        elif i[0] == "A":
            numbers_list.append(14)
        else:
            numbers_list.append(int(i[0]))
    else:
        numbers_list.append(10)

# Check for Royal
royal_check = None
if ("10" in situation_1_string) \
        and ("J" in situation_1_string) \
        and ("Q" in situation_1_string) \
        and ("K" in situation_1_string) \
        and ("A" in situation_1_string):
    royal_check = True
else:
    royal_check = False

# Check for Flush
flush_check = None
h = 0
d = 0
c = 0
s = 0
for i in player_1_situation:
    if i[-1] == "♡":
        h += 1
    elif i[-1] == "♢":
        d += 1
    elif i[-1] == "♧":
        c += 1
    elif i[-1] == "♤":
        s += 1
if h == 5 or d == 5 or c == 5 or s == 5:
    flush_check = True
else:
    flush_check = False

# Check for Straight
straight_check = None
nodupl_numbers = []
for i in numbers_list:
    if i not in nodupl_numbers:
        nodupl_numbers.append(i)
nodupl_numbers.sort()
number_next_to = 0
for i in range(0, len(nodupl_numbers)-1):
  if nodupl_numbers[i+1] - nodupl_numbers[i] == 1:
    number_next_to += 1
    if number_next_to == 4:
      straight_check = True
      break
    else:
      straight_check = False
  else:
    number_next_to *= 0
    straight_check = False
else:
    straight_check = False

# Check for Duplicates / Triples / Quadruples
all_multiples = []
for i in numbers_list:
    count = numbers_list.count(i)
    all_multiples.append(count)
max_multiples = max(all_multiples)

# Playing and Evaluating Hand
print("Community Cards:   " + community_string)
print("Your Hand:         " + player_1_string + "\n\n")

if (royal_check == True) and (flush_check == True):
    print("Royal Flush        Probability:  0.0002%")
elif flush_check == True and straight_check == True:
    print("Straight Flush     Probability:  0.0014%")
elif max_multiples == 4:
    print("Four of a Kind     Probability:  0.024%")
elif (3 in all_multiples) and (2 in all_multiples):
    print("Full House         Probability:  0.1441%")
elif flush_check is True:
    print("Flush              Probability:  0.198%")
elif straight_check is True:
    print("Straight           Probability:  0.39%")
elif max_multiples == 3:
    print("Three of a Kind    Probability:  2.11%")
elif all_multiples.count(2) == 4:
    print("Two Pairs          Probability:  4.79%")
elif max_multiples == 2:
    print("One Pair           Probability: 42.3%")
else:
    print("High Card          Probability: 50.1%")

print("\n\n\nComment your best hand!")

"""
# Testing (print if you like)
print("\n\ntesting:")
print("numbers list:          " + str(numbers_list))
print("noduplicates list:     " + str(nodupl_numbers))
print("royal check:           " + str(royal_check))
print("flush check:           " + str(flush_check))
print("straight check:        " + str(straight_check))
print("all multiples check:   " + str(all_multiples))
"""

