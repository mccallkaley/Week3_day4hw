import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# deck has to be created with EMPTY  list and needs to shuffle and deal
# deck needs a constructor method for each deck (suit,ranks)
# Need a method to get deck of cards and shuffle deck 

class Deck:

    def __init__(self):
        self.deck = [] # empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = '' #starting other player(competitions) deck empty
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # add each card objects string value
        return 'The deck has' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card  

# HAND will initilize itself, can be added to + value of ACE 1 or 11 adjusted based on what score is 

class Hand:
    def __init__(self):
        self.cards = [] # start off with Empty list 
        self.value = 0
        self.aces = 0 # ADD an attribute to keep track of aces 

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1
    

# a function that could be used in the game                  
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Player will either need to hit or stand depending on what values they already have to get close to 21 and we need a func for them to apply this
def hit_or_stand(deck,hand):
    global playing 
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        # want to make it so they can do h or  hit and both work 
        if x[0].lower() == 'h':   #use hit func right above
            hit(deck,hand) 
        # want to make it so they can do s or  Stand and both work
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

#functions to DISPLAY CARDS FOR DEALER AND PLAYER!

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>", sep = '\n')
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
        
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

#functions to handle game scenarios#
def player_busts(player,dealer):
    print("Player busts! We are taking your money and the Dealer wins!")

def player_wins(player,dealer):
    print("Congrats! Player wins! Here is some money so you become addicted to gambling!")

def dealer_busts(player,dealer):
    print("Dealer busts! Player wins! Here is some money so you become addicted to gambling!")
    
def dealer_wins(player,dealer):
    print("Sorry Player! We are taking your money and the Dealer wins!")
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")    

playing = True

while True:
    # Print an opening statement
    print("Let's play Blackjack!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    show_some(player_hand, dealer_hand)

    while playing:  
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand) 
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value <17:
            hit(deck, dealer_hand)
        # Show all cards
        show_all(player_hand,dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand)
        else:
            push(player_hand,dealer_hand)


    # Will ask to play again
    new_game = input("would you like to play again? Enter 'y' or 'n'")
    # if the person types yes or 'y' this will work because its first index
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing my blackjack game! ')

        break