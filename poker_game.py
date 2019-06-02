import random
import math
import sys

# define each card
class Card(object):

    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    suits = ('S', 'D', 'H', 'C')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def face_card (self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit


    def greater_equal (self, other):
        return (self.rank >= other.rank) 

    def less_equal (self, other):
        return (self.rank <= other.rank)

    def greater_than (self, other):
        return (self.rank > other.rank)

    def less_than (self, other):
        return (self.rank < other.rank)

    def same(self, other):
        return self.rank == other.rank

    def not_same (self, other):
        return (self.rank != other.rank)


# create deck and deal mechanism
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.suits:
      for rank in Card.ranks:
        card = Card (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)


# create poker game
class Poker (object):
  def __init__ (self, numHands):
    self.deck = Deck()
    self.deck.shuffle ()
    self.hands = []
    self.tlist=[]       
    how_many_cards_in_hand = 5

    for i in range (numHands):
      hand = []
      for j in range (how_many_cards_in_hand):
        hand.append (self.deck.deal())
      self.hands.append(hand)
  
  
  def play (self):
    counter = 1
    for hand in self.hands:
        print(("Player {}\n").format(counter))
        for card in hand:
            print((card.face_card()) + ' ')
        counter += 1
        print('\n') 
      
  def point(self,hand):                         
    sortedHand=sorted(hand,reverse=True)
    rank_order = []
    for card in sortedHand:
      rank_order.append(card.rank)
    return rank_order[0]


  def isHigh (self, hand):                         
    sortedHand=sorted(hand,reverse=True)
    total_point=self.point(sortedHand)
    mylist=[]                                    
    for card in sortedHand:
      mylist.append(card.rank)
    self.tlist.append(total_point)
        
        

if __name__ == "__main__":
    numHands = int(sys.argv[1])
    game = Poker (numHands)
    game.play()  
    print('\n')
    for i in range(numHands):
        curHand=game.hands[i]
        print ("Hand "+ str(i+1) + " " )
        game.isHigh(curHand)

    maxpoint=max(game.tlist)
    maxindex=game.tlist.index(maxpoint)

    print ('\nHand %d wins'% (maxindex+1))
  