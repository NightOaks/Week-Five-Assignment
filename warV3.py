#War Version 1.0

#Devin Simoneaux

#This is war according to Version 3 in the README file

import random	

def main():
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0
	cardA = 0
	cardB = 0
	rankA = 0
	rankB = 0


	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	
	# Gets a card from each player
	cardA = PlayerA.pop()
	cardB = PlayerB.pop()
	
	# Gets the rank of each card
	
	rankA = getRank(cardA)
	rankB = getRank(cardB)
	
	# Determine the winner
	if rankA > rankB:
		PlayerA.insert(0, cardA)
		PlayerA.insert(0, cardB)
	elif rankB > rankA:
		PlayerB.insert(0, cardB)
		PlayerB.insert(0, cardA)
	else:
		# Find out if each player has enough to do a WAR
		if len(PlayerA) < 4:
			PlayerA = []
			print("Player B wins!")
		elif len(PlayerB) < 4:
			PlayerB = []
			print("Player A wins!")
		else:
			PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
		
	savedCardsA = []
	savedCardsB = []
	warCardA = 0
	warCardB = 0
	rankWarA = 0
	rankWarB = 0
	
	# Saves the top 3 cards in each player's deck
	for i in range(0,3):
		savedCardsA.append(PlayerA.pop())
		savedCardsB.append(PlayerB.pop())
	
	# Gets a war card from each player's deck
	warCardA = PlayerA.pop()
	warCardB = PlayerB.pop()
	
	# Gets the rank of each war card
	rankWarA = getRank(warCardA)
	rankWarB = getRank(warCardB)
	
	# Determine the winner
	if rankWarA > rankWarB:
		PlayerA.insert(0, warCardA)
		PlayerA.insert(0, warCardB)
		PlayerA = savedCardsA + PlayerA
		PlayerA = savedCardsB + PlayerA
	elif rankWarB > rankWarA:
		PlayerB.insert(0, warCardB)
		PlayerB.insert(0, warCardA)
		PlayerB = savedCardsB + PlayerB
		PlayerB = savedCardsA + PlayerB
	else:
		print("This WAR is over.")
	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

