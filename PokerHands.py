hands = ["1H", "4H", "4H", "1H", "2H"]
handsNums = [0]*5
handsSuit = [0]*5

def num_to_value(card):
	print card,
	if card == "T" : return 10
	elif card == "J" : return 11
	elif card == "Q" : return 12
	elif card == "K" : return 13
	elif card == "A" : return 14
	else: return int(card)

def suit_to_value(card):
	print card,
	if card == "C" : return 1
	elif card == "S" : return 2
	elif card == "D" : return 3
	elif card == "H" : return 4



def is_straight(hand):
	if hand == [hand[0],hand[0]+1,hand[0]+2,hand[0]+3,hand[0]+4]:
		print "Straight"
		return True

def is_flush(hand):
	clubs = [1,1,1,1,1]
	spades = [2,2,2,2,2]
	diamonds = [3,3,3,3,3]
	hearts = [4,4,4,4,4]
	if (hand == clubs or hand == spades or hand == diamonds or hand == hearts):
		return True

def is_royal_flush(hand):
	royal = [10,11,12,13,14]
	if sum(hand) % sum(royal) == 0 :
		return True

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

def is_full_house(hand):
	card1, card2 = hand[0], 0
	cardCount1,	cardCount2 = 0,0
	card2 = 0
	for i in range(0,5):
		if hand[i] == card1:
			cardCount1+=1
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
		return True
	return False

def is_pair(hand):
	for i in range(0,5):
		test = hand[i]
		for j in range(i+1,5):
			if hand[j] == test:
				return True

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
	if cardCount1 == 3 or cardCount2 == 3 or cardCount3 == 3:
		return True
	return False

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
	print cardCount1,
	print cardCount2,
	print cardCount3
	if (cardCount1==2 and cardCount2==2) or (cardCount1==2 and cardCount3==2) or (cardCount2==2 and cardCount3==2):
		return True
	return False



#Convert data to readable format
for i in range(0,5):
	handsNums[i] = num_to_value(hands[i][0])
	handsSuit[i] = suit_to_value(hands[i][1])
print ""


#Test for Straight, Straight Flush, Royal Flush
if is_straight(handsNums):
	if is_flush(handsSuit):
		if is_royal_flush(handsNums):
			print "Royal Flush"
		else: print "Straight Flush"
	else: print "Straight"

#Test for pairs
if is_pair(handsNums):
	print "Pair"
	if is_two_pair(handsNums):
		print "Two pair"
	if is_three_of_a_kind(handsNums):
		print "Three of a Kind"
	#is_four_of_a_kind(handsNums)
	#is_full_house

if is_four_of_a_kind(handsNums):
	print "Four of a Kind"

if is_full_house(handsNums):
	print "Full House"

if is_flush(handsSuit):
	print "Flush"

#Set up first, then optimize later