
import cardfactory as cardfact
import card as card
import deck as deck


def play_round(deck1, deck2):

    war_iteration = 0  # initialize war iterations
    compare_card_1 = deck1.draw()
    compare_card_2 = deck2.draw()
    print("player 1's card ordinal : {}    ".format(compare_card_1.ordinal))
    print("player 2's card ordinal : {}".format(compare_card_2.ordinal))
    if compare_card_1.ordinal > compare_card_2.ordinal:
        print("(player 1 ordinal : {} > {} : player 2 ordinal) hence player 1 wins this round"
              .format(compare_card_1.ordinal, compare_card_2.ordinal))
        print("\n")
        deck1.discard_pile.append(compare_card_1)
        deck1.discard_pile.append(compare_card_2)
    elif compare_card_2.ordinal > compare_card_1.ordinal:
        print("(player 1's ordinal : {} < {} player 2's ordinal) hence player 2 wins this round"
              .format(compare_card_1.ordinal, compare_card_2.ordinal))
        print("\n")
        deck2.discard_pile.append(compare_card_1)
        deck2.discard_pile.append(compare_card_2)
    else:  # war happens

        war_cards_pot = []  # initialize a war pot
        while True:
            if compare_card_1.ordinal != compare_card_2.ordinal:  # if compare cards are not equal war ends
                break
            war_iteration += 1
            num_deck1 = deck1.get_num_cards()  # get number of remaining cards in player 1's deck.
            if num_deck1 >= 2:
                war_cards_pot.append(compare_card_1)  # add previous war iteration compare card to war_cards_pot
                war_cards_pot.append(deck1.draw())  # draw 2 cards, add first to war_cards_pot, use 2nd as compare card
                compare_card_1 = deck1.draw()
            elif num_deck1 == 1:  # just one card left to draw for player 1
                war_cards_pot.append(compare_card_1)  # add previous war iteration compare card to war_cards_pot
                compare_card_1 = deck1.draw()
            else:  # no more cards to draw for player1, use last war iteration's compare card for comparision again
                pass

            num_deck2 = deck2.get_num_cards()
            if num_deck2 >= 2:
                war_cards_pot.append(compare_card_2)  # add previous war iteration compare card to war_cards_pot
                war_cards_pot.append(deck2.draw())  # draw 2 cards add first to pot, use second card as comparision card
                compare_card_2 = deck2.draw()
            elif num_deck2 == 1:
                war_cards_pot.append(compare_card_2)  # add previous war iteration compare card to war_cards_pot
                compare_card_2 = deck2.draw()
            else:  # no more cards to draw for player 2, use last war iteration's compare card for comparision again
                pass

        war_cards_pot.append(compare_card_1)
        war_cards_pot.append(compare_card_2)
        if compare_card_1.ordinal > compare_card_2.ordinal:  # player 1 wins war, collects war_cards_pot and adds
            # war_cards_pot to discard pile
            print("player 1's card ordinal  : {} > {} : player 2's card ordinal hence player 1 wins this round of war"
                  .format(compare_card_1.ordinal, compare_card_2.ordinal))
            print("war iterations == {}".format(war_iteration))
            deck1.discard_pile.extend(war_cards_pot)
            print("total number of cards  =={}(remaining cards in deck 1)+"
                  "{}(remaining cards in deck 2) == {}".format(deck1.get_num_cards(), deck2.get_num_cards(),
                                                               deck1.get_num_cards() + deck2.get_num_cards()))

        if compare_card_1.ordinal < compare_card_2.ordinal:  # player 2 wins war, collects war_cards_pot and
            # adds it to discard pile
            print("player 1's card ordinal  : {} < player 2's card ordinal: {} hence player 2 wins this round of war"
                  .format(compare_card_1.ordinal, compare_card_2.ordinal))
            print("war iterations == {}".format(war_iteration))
            deck2.discard_pile.extend(war_cards_pot)
            print("total number of cards  == {}(remaining cards in deck 1)+"
                  "{}(remaining cards in deck 2) == {}".format(deck1.get_num_cards(), deck2.get_num_cards(),
                                                               deck1.get_num_cards() + deck2.get_num_cards()))
        return war_iteration



def play_game(player1, player2):
    """
    This function when called will play an entire game of War.
    playRound will get called until either play is completely out of cards.
    
    :param player1: Deck of cards representing player 1
    :param player2: Deck of cards representing player 2
    """
    iteration = 0
    wars = {}
    while player1.get_num_cards() > 0 and player2.get_num_cards() > 0:
        print("game is on {} iteration, player1 has {} remaining cards"
              "player 2 has {} remaining cards"
              "total cards are equal to {} ".format(iteration, player1.get_num_cards(), player2.get_num_cards()
            , (player1.get_num_cards()+player2.get_num_cards())))
        print("\n")
        war_iterations = play_round(player1, player2)
        if war_iterations in war:
            wars[war_iterations] += 1
        else:
            wars[war_iterations] = 1
        
    return iteration, wars

if __name__== '__main__':

    total_iterations = 0
    wars = {}
    for i in range(10000):
        factory = cardfact.CardFactory()

        # Makes a full deck for p1, empty for p2, shuffles
        player1 = factory.create_full_deck()
        player2 = deck.Deck()
        player1.shuffle()

        # Deals half of player 1's shuffled deck to player 2
        decksize = int(player1.get_draw_pile_size() / 2)
        for i in range(decksize):
            player2.add_to_discard(player1.draw())

        # Shuffle the decks
        player1.shuffle()
        player2.shuffle()
        iteration, wars = play_game(player1, player2)
        total_iterations += iteration

    average_iterations = (total_iterations/10000)
    print("After simulating the game 10000 times, the average number of iterations i.e" +
         "number of times play_round is called per call to play_game is {}".format(average_iterations))
    for keys in wars:
        print("wars of {} iterations occured {} times".format(keys, wars[keys]))
