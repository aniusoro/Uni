#LAB 5: ANIETIE AKPANUSOH (1628270)

import random
#import pygame
class Card(object):
    #Initializes our card class with a rank and category
    def __init__(self, rank, category):
        self.rank = rank
        self.category = category
    
    #returns the rank of a card
    def get_rank(self):
        return self.rank
    
    #returns the category of a card
    def get_category(self):
        return self.category
    
    #displays a card
    def display(self):
        print ("|{}{}|".format(self.rank, self.category))

        
class Deck(object):
    #Initialize our deck class, by generating all the different possible cards (using the Card class) we could have in our 16 card deck
    def __init__(self):
        self.cards = []
        for i in ['C', 'D', 'T', 'M']:
            for s in range(1,5):
                self.cards.append(Card(s,i))
    
    #Randomly shuffle the decks of cards
    def shuffle(self):
        random.shuffle(self.cards)
    
    #Return a value from the top of the deck, remember to remove it from the deck as well.
    def deal(self):
        card = self.cards.pop(0)
        return card
    
    #Display the remaining cards in the deck
    def display(self):
        for x in range(len(self.cards)):
            self.cards[x].display()
                
                
class Player(object):
    #Initializes a player with a way of keeping track of cards in their hand.
    def __init__(self):
        self.hand = []
     
    
    def add(self, card):
        self.hand.append(card)
    
    
    def cards_of_category(self, category):
        total = 0
        for y in range(len(self.hand)):
            if self.hand[y].get_category()==category:
                total += self.hand[y].get_rank()
        
        return total
        
    
    def display(self):
        for a in range(len(self.hand)):
            self.hand[a].display()
        
    
                
                

def main():
    #This creates a deck
    deck = Deck()
    #This shuffle the deck
    deck.shuffle()
    #This creates the hand of the player
    player = Player()
    #This inserts 5 cards from the deck into hand
    for i in range(5):
        player.add(deck.deal())
    print("This is the player hand")
    player.display()
    #This displays the players hands
    print("This is the rest of the deck")
    deck.display()
    #This is when we input the catergory to be added up
    category = input("Select a category (C,D,T,M):").upper()
    #This adds up the sum of the numbers in the category that is inputed. 
    print ("The sum of {} cards in the player's hand is: {}".format(category,player.cards_of_category(category)))


#This calls the main function for the program to be run. 
main()
            
