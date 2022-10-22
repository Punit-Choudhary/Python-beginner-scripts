#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$BLACKJACK GAME$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting.

###rules###
#blackjack, or twenty-one, Card game whose object is to be dealt cards having a higher count than those of the dealer, up to but not exceeding 21.
#The dealer may use a single deck of 52 cards or two or more decks from a holder called a shoe
#Aces count as 1 or 11, and face cards as 10.
#If you enter yes to HIT you will only if you have higher count than dealer but still lower than 21
#If you enter no to HIT you can continue until next turn given another chance to hit after getting another card, goes on until win or loss
#Initially player and broker will get two cards
#In each no to HIT sequence another card will be added to both player and broker
#Player's all cards will be visible but broker's one card will be visible throughout

from random import shuffle
class card():
    def __init__(self,sym,num):
        self.sym = sym
        self.num = num
        self.value = values[self.num]
    def __str__(self):
        return self.num + " of " + self.sym


'''using oop'''
symbols = ('spade','hearts','clubs','diamond')
numbers = ('ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king')
values = {'two': 2,'three' : 3,'four' : 4,'five' : 5, 'six':6,'seven':7,'eight':8,'nine':9,'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':1}


class Deck:
    def __init__(self):
        # for creating the all the cards neccessary for game
        self.all_cards = []
        for num in numbers:
            for sym in symbols:
                created_card = card(sym, num)
                self.all_cards.append(created_card)

    def Shuffle(self):
        # to  shuffle all the cards for playing
        shuffle(self.all_cards)

    def one_card(self):
        # to remove the card in game
        return self.all_cards.pop(0)



# hold cards
# both open i.e to print all the cards the player holds
# coins
# limit is 21
# the opposite will if player busts i.e exceeds sumofcards value 21
# choice of hit and condition for bust
# nearer condition where the person near to their limit may win(doubt)



class Player(Deck):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.allcards = []
        self.earnings = 0
        self.sump = 0
        self.deposit = 1
        for i in range(len(self.allcards)):
            self.sump += self.allcards[i].value

    # here I used deck inheritance to

    def sums(self):
        for i in range(len(self.allcards)):
            self.sump += self.allcards[i].value

    def Add_card(self, new):
        pass

    def Bust(self):


        for i in range(len(self.allcards)):
            self.sump += self.allcards[i].value

        if self.sump > 21:
            print("Better Luck Next Time!!")
            return True
        else:

            return False

    def Deposit(self):
        deposit = ''
        while deposit.isdigit() == False:
            deposit = (input("Enter you betting a amount: "))
        deposit = int(deposit)
        self.deposit = deposit

    def Win(self):
        print("you've won the game")
        self.earnings += 2 * self.deposit
        print(f"In this round you've earned ${self.earnings}")

    def Lose(self):
        print("you've lost the game")
        self.earnings -= self.deposit
        print(f"In this round you've lost ${self.earnings}")

    def print_all(self):
        for i in range(len(self.allcards)):
            print(f"{i + 1}) {self.allcards[i]}")

    # add a __str__ dunder method here for printing players cards

    def __str__(self):

        return f"self.name has {len(self.allcards)} and won {self.earnings}"


# holds cards
# one open and other closed
# coins
# limit is 17
# the opposite will if player busts i.e exceeds sumofcards value 17
# choice of hit and condition for bust
# nearer condition where the person near to their limit may win(doubt)
class Broker():

    def __init__(self, name):
        self.name = name
        self.bcards = []
        self.sumb = 0

    def sums(self):
        for i in range(len(self.bcards)):
            self.sumb += self.bcards[i].value

    def Add_card(self, new):

        self.bcards.append(new)
        print("added a new card to broker")

    def Bust(self):
        for i in range(len(self.bcards)):
            self.sumb += self.bcards[i].value

        if self.sumb >= 17:
            print(self.sumb)

            return True and self.sumb
        else:
            print(f"sum of broker's cards: {self.sumb}")
            return False

    def Showb(self):
        for i in range(1):
            print(f"Broker Cards: {self.bcards[i]}")


"""ADD THE FUNCTIONALITY OF HIT"""
"""ADD THE FUNCTIONALITY OF CONSIDERING ACE VALUE AS BOTH 1 OR 11 BASED ON SITUATION """
"""CREATE A METHOD FOR PLAYER WHICH CHECKS WHICH VALUE OF ACE BETTER SUITS THE INSTANCE IE IF SUMP >21 THEN  ACE.VALUE = 1 OR WHEN EVENING TAKING ACE.VALUE = 11 THEN TOO THE SUMP WON'T EXCEED 21 IN THIS CASE DDEFINITELY TAKE THIS+"""



#final game func
def Game():
    ## GAme Logic
    rnd = 0
    cash = 0

    ex = False

    def ace():
        for i in range(len(plyr.allcards)):
            if plyr.allcards[i].value == 1:
                if plyr.Bust() == True:
                    plyr.allcards[i].value = 11
                else:
                    pass
        for i in range(len(brkr.bcards)):
            if brkr.bcards[i].value == 1:
                if brkr.Bust() == True:
                    brkr.bcards[i].value = 11
                else:
                    pass

    #####################################################################################################################

    def exit_call():
        print(f"you've earned {cash} in {rnd} rounds")
        exit()

    while ex == False:
        plyr = Player("Player ")
        brkr = Broker("Broker")
        plyr.Deposit()
        game_on = True
        new_deck = Deck()
        new_deck.Shuffle()
        for i in range(2):
            plyr.allcards.append(new_deck.one_card())
            brkr.bcards.append(new_deck.one_card())

        rnd += 1
        print(f"round:{rnd}")

        def hit(cash):
            x = ''
            while x not in ["yes", "no"]:
                x = input(f"Do you wanna hit Player(yes | no):  ").lower()
                addp = plyr.sump - 21
                addb = brkr.sumb - 17
            if x == "yes":
                # find a  way to find who is close to their target number plyr or broker
                if addp < 0 and addb < 0:
                    # cause the person having more difference will lose
                    if abs(addp) < abs(addb):

                        plyr.Win()
                        play = False
                        game_on = False
                        quit()


                    else:
                        plyr.Lose()

                        play = False
                        game_on = False
                        quit()

                elif plyr.sump >21:
                    plyr.Lose()
                    play = False
                    game_on = False
                    quit()

                elif addp > 0 and addb > 0:
                    plyr.Lose()

                    play = False
                    game_on = False
                    quit()




                elif addp > 0 and addb < 0:
                    plyr.Lose()

                    play = False
                    game_on = False
                    quit()


                elif addp < 0 and addb > 0:
                    plyr.Win()

                    play = False
                    game_on = False
                    quit()

                """"if addp > 0 and addb < 0:
                    plyr.Win()
                    play = False
                    exit()
                elif abs()
                else:
                    plyr.Lose()
                    play = True
                    exit()"""
                return True
            else:
                return False

        ###########################################################################################################################
        while game_on:
            plyr.sump = 0
            brkr.sumb = 0
            plyr.sums()
            brkr.sums()
            plyr.print_all()
            brkr.Showb()
            # print(plyr.sump)

            plyr.sump = 0
            brkr.sumb = 0

            if plyr.Bust():
                print(f"your cards sum {plyr.sump} exceeds 21")
                plyr.Lose()
                cash += plyr.earnings
                ex = exit_call()
                game_on = False
                break


            else:
                play = True
                while play:

                    plyr.print_all()
                    brkr.Showb()

                    ace()
                    n = hit(cash)
                    if n == True:
                        cash = cash + plyr.earnings
                        ex = exit_call()
                        game_on = False
                        break


                    if n == False:
                        plyr.allcards.append(new_deck.one_card())
                        brkr.bcards.append(new_deck.one_card())
                        plyr.print_all
                        break

if __name__ == "__main__":
    Game()



