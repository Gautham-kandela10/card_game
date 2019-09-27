"""
Knexus Python Programming test

Author: JT
"""
import cardfactory as cardfact
import card as card
import deck as deck


def play_round(deck1, deck2):

    war_iteration = 0  # initialize war iterations
    
    compare_card_1 = deck1.draw()
    compare_card_2 = deck2.draw()
    
    if compare_card_1.ordinal > compare_card_2.ordinal:  # player 1 wins round
        deck1.discard_pile.append(compare_card_1)
        deck1.discard_pile.append(compare_card_2)
    elif compare_card_2.ordinal > compare_card_1.ordinal:  # player 2 wins round
        deck2.discard_pile.append(compare_card_1)
        deck2.discard_pile.append(compare_card_2)
    else:  # war happens
        war_cards_pot = []  # initialize a war pot
        while True:
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
            if compare_card_1.ordinal != compare_card_2.ordinal:  # if compare cards are not equal war ends
                break

        war_cards_pot.append(compare_card_1)
        war_cards_pot.append(compare_card_2)
        if compare_card_1.ordinal > compare_card_2.ordinal:  # player 1 wins war, collects war_cards_pot in discard pile
            deck1.discard_pile.extend(war_cards_pot)
        if compare_card_1.ordinal < compare_card_2.ordinal:  # player 2 wins war, collects war_cards_pot in discard pile
            deck2.discard_pile.extend(war_cards_pot)



def play_game(player1, player2):
    """
    This function when called will play an entire game of War.
    playRound will get called until either play is completely out of cards.
    
    :param player1: Deck of cards representing player 1
    :param player2: Deck of cards representing player 2
    """
    
    while player1.get_num_cards() > 0 and player2.get_num_cards() > 0:
        play_round(player1, player2)

if __name__== '__main__':
    # Creates the card factory
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

    # play a single round of War
    play_round(player1, player2)

    # play an entire game of War
    #play_game(player1, player2)