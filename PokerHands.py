import time

#Convert data to value
def num_to_value(card):
	if card == "T" : return 10
	elif card == "J" : return 11
	elif card == "Q" : return 12
	elif card == "K" : return 13
	elif card == "A" : return 14
	else: return int(card)
def suit_to_value(card):
	if card == "C" : return 1
	elif card == "S" : return 2
	elif card == "D" : return 3
	elif card == "H" : return 4

#Winning Hands
def is_pair(hand):
	for i in range(0,5):
		card = hand[i]
		for j in range(i+1,5):
			if hand[j] == card:
				return True, card
def is_two_pair(hand):
	card1 = hand[0]
	card2,card3 = 0,0
	cardCount1,cardCount2,cardCount3 = 0,0,0
	for i in range(0,5):
		if hand[i] == card1 : cardCount1+=1
		else:
			card2 = hand[i]
			cardCount2+=1
			break
	for j in range(i+1,5):
		if hand[j] == card1 : cardCount1+=1
		elif hand[j] == card2 : cardCount2+=1
		else:
			card3 = hand[j]
			cardCount3+=1
			break
	for k in range(j+1,5):
		if hand[k] == card1 : cardCount1+=1
		elif hand[k] == card2 : cardCount2+=1
		elif hand[k] == card3 : cardCount3+=1
		else: return False
	if (cardCount1==2 and cardCount2==2): return True, max(card1,card2)
	elif (cardCount1==2 and cardCount3==2): return True, max(card1,card3)
	elif (cardCount2==2 and cardCount3==2): return True, max(card2,card3)
	return False
def is_three_of_a_kind(hand):
	card1 = hand[0]
	card2,card3 = 0,0
	cardCount1,cardCount2,cardCount3 = 0,0,0
	for i in range(0,5):
		if hand[i] == card1 : cardCount1+=1
		else:
			card2 = hand[i]
			cardCount2+=1
			break
	for j in range(i+1,5):
		if hand[j] == card1 : cardCount1+=1
		elif hand[j] == card2 : cardCount2+=1
		else:
			card3 = hand[j]
			cardCount3+=1
			break
	for k in range(j+1,5):
		if hand[k] == card1 : cardCount1+=1
		elif hand[k] == card2 : cardCount2+=1
		elif hand[k] == card3 : cardCount3+=1
		else: return False
	if cardCount1 == 3: return True, card1
	elif cardCount2 == 3: return True, card2
	elif cardCount3 == 3: return True, card3
	return False
def is_straight(hand):
	if hand == [hand[0],hand[0]+1,hand[0]+2,hand[0]+3,hand[0]+4]:
		return True
def is_flush(hand):
	clubs, spades, diamonds, hearts = [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3], [4,4,4,4,4]
	if (hand == clubs or hand == spades or hand == diamonds or hand == hearts):
		return 5, "Flush", hand[0]
def is_full_house(hand):
	card1, card2 = hand[0], 0
	cardCount1,	cardCount2 = 0,0
	card2 = 0
	for i in range(0,5):
		if hand[i] == card1: cardCount1+=1
		else:
			card2 = hand[i]
			cardCount2+=1
			break
	for j in range(i+1,5):
		if hand[j] == card1:
			cardCount1+=1
		elif hand[j] == card2:
			cardCount2+=1
		else: return False
	if (cardCount1 == 3 and cardCount2 == 2) or (cardCount1 == 2 and cardCount2 == 3):
		return True, max(card1,card2)
	return False
def is_four_of_a_kind(hand):
	if (hand[0] == hand[1] or hand[0] == hand[2]):
		test = hand[0]
	elif (hand[1] == hand[0] or hand[1] == hand[2]):
		test = hand[1]
	else: return False
	count=0
	for i in range(0,5):
		if hand[i] == test:
			count+=1
	if count == 4:
		return True
	return False
def is_royal_flush(hand):
	royal = [10,11,12,13,14]
	if sum(hand) % sum(royal) == 0 :
		return True

#Test for Straight, Straight Flush, Royal Flush
def is_ordered(handNums,handSuit):
	if is_straight(handNums):
		if is_flush(handSuit):
			if is_royal_flush(handNums):
				return 9, "Royal Flush", handSuit[0]
			else: return 8, "Straight Flush", handNums[4]
		else: return 4, "Straight", handNums[4]

#Test for pairs
def is_paired(handNums):
	if is_pair(handNums):
		if is_three_of_a_kind(handNums):
			if is_full_house(handNums):
				return 6, "Full House", is_full_house(handNums)[1]
			return 3, "Three of a kind", is_three_of_a_kind(handNums)[1]
		if is_four_of_a_kind(handNums):
			return 7, "Four of a Kind", is_four_of_a_kind(handNums)[1]
		if is_two_pair(handNums):
			return 2, "Two pair", is_two_pair(handNums)[1]
		return 1, "Pair", is_pair(handNums)[1]

def high_card(handNum):
	return 0, "High Card", max(handNum)


#Program Outline
p1Wins,p2Wins = 0,0
p1HandsNums, p1HandsSuit = [0]*5, [0]*5
p2HandsNums, p2HandsSuit = [0]*5, [0]*5

start = time.time()

#1 READ THE DATA
allHands = []
with open('data/poker-data.txt') as f:
	for line in f:
		allHands.append([x for x in line.rstrip('\n').split(" ")])

for x, hands in enumerate(allHands):
	#2 CONVERT DATA TO READABLE FORMAT
	for i in range(0,5):
		p1HandsNums[i] = num_to_value(hands[i][0])
		p1HandsSuit[i] = suit_to_value(hands[i][1])

		p2HandsNums[i] = num_to_value(hands[i+5][0])
		p2HandsSuit[i] = suit_to_value(hands[i+5][1])

	#3 FIND WINNING HAND
	player1 = max([high_card(p1HandsNums), is_ordered(p1HandsNums,p1HandsSuit), is_paired(p1HandsNums), is_flush(p1HandsSuit)])
	player2 = max([high_card(p2HandsNums), is_ordered(p2HandsNums,p2HandsSuit), is_paired(p2HandsNums), is_flush(p2HandsSuit)])

	print "\nHAND " + str(x+1)
	print player1[1],
	print player1[2]
	print player2[1],
	print player2[2]

	#4 COMPARE WINNING HAND
	if (player1[0] == player2[0]) : print "TIE",
	if ((player1[0] > player2[0]) or 
			(player1[0] == player2[0]) and (player1[2] > player2[2])):	
		p1Wins+=1
		print "PLAYER 1 WINS"
	else:
		p2Wins+=1
		print "PLAYER 2 WINS"

elapsed = time.time() - start

print "Total Player 1 Wins: " + str(p1Wins)
print "Elapsed time %s" % (elapsed)