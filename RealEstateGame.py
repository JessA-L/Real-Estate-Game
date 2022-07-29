# Author: Jessica Allman-LaPorte
# GitHub username: JessicaAllman-LaPorte
# Date: 7/28/2022
# Description:

class GameSpace(object):
    """Represents a game space the player can land on"""
    def __init__(self, amount):
        self._space_amount = amount
        self._space_name = ""
        self._purchase_price = amount*5

    def get_rent_amount(self):
        """
        returns amount that must be paid when non-owner player lands
        on space or the amount paid to player when passing GO
        """
        return self._space_amount

    def get_purchase_price(self):
        """returns purchase price"""
        return self._purchase_price

    def set_purchase_price(self, purchase_price):
        """sets purchase price of item"""
        self._purchase_price = purchase_price

    # def get_name(self):
    #     """returns name of space"""
    #     return self._space_name
    #
    # def set_name(self, space_name):
    #     """
    #     sets name of game space
    #     :param space_name:
    #     :return:
    #     """
    #     self._space_name = space_name


class RealEstateGame(object):

    # create_spaces - takes two parameters: the amount of money given to players when they
    #   land on or pass the "GO" space, and an array of 24 integers (rent amounts)
    def __init__(self):
        self._spaces_dict = {}
    def create_spaces(self, pass_go_amount, rent_amounts_array):
        """
        Creates game spaces and assigns rent to space
        :param pass_go_amount:
        :param rent_amounts_array:
        :return: None
        """
        # Creates a space named "GO". This space cannot be purchased by any player
        self._spaces_dict['space_go'] = GameSpace(pass_go_amount)
        self._spaces_dict['space_go'].set_purchase_price(None)  # sets go_space purchase price to None
        print(self._spaces_dict['space_go'].get_purchase_price())

        # Creates exactly 24 more game spaces (for a total of 25):
            # Spaces must not have duplicate names
            # Spaces will have rent amounts initialized from the array of 24 rent values.
            # Each space will have a purchase price equal to 5 times the rent amount

        for i in range(24):
            self._spaces_dict['space_' + str(i+1)] = GameSpace(rent_amounts_array[i])
        print(self._spaces_dict)

    # create_player - takes two parameters: a unique name and an initial account balance
        # Players always start at the "GO" Space

    # get_player_account_balance - takes as a parameter the name of the player and
    #   returns the player's account balance

    # get_player_current_position - takes as a parameter the name of the player and
    #   returns the player's current position on the board as an integer (where the "GO" space is position zero)

    # buy_space - takes as parameters the name of the player
        # If the player has an account balance greater than the purchase price,
        #   and the space doesn't already have an owner:
            # The purchase price of the space will be deducted from the player's account
            # The player is set as the owner of the current space
            # The method returns True
        # Otherwise, the method returns False

    # move_player - takes as parameters the name of the player, and the number of spaces to move
        # If the player's account balance is 0, the method will return immediately without
        #   doing anything
        # The number of spaces to move will be an integer between 1 and 6
        # The method will advance the player around the circular board by the number of spaces
        # If the player lands on or passes "GO" while being moved, the player receives the
        #   "GO" amount of money
        # After the move is complete the player will pay rent for the new space occupied,
        #   if necessary
            # No rent will be paid if the player is occupying the "GO" space,
            #   or if the space has no owner, or if the owner is the player
            # Otherwise:
                # The player must pay the rent for the space currently occupied
                # The player will not pay more than the amount in player's account balance
                # The amount paid is deducted from the players account and deposited into the game space owner's account
                # If the player's new account balance is 0, the player has lost the game, and must be removed as the owner of any spaces.

    # check_game_over - takes no parameters
        # The game is over if all players but one have an account balance of 0
        # If the game is over, the method returns the winning player's name
        # Otherwise, the method returns an empty string

if __name__ == "__main__":
    game = RealEstateGame()

    rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
             350, 350]
    game.create_spaces(50, rents)
    #
    # game.create_player("Player 1", 1000)
    # game.create_player("Player 2", 1000)
    # game.create_player("Player 3", 1000)
    #
    # game.move_player("Player 1", 6)
    # game.buy_space("Player 1")
    # game.move_player("Player 2", 6)
    #
    # print(game.get_player_account_balance("Player 1"))
    # print(game.get_player_account_balance("Player 2"))
    #
    # print(game.check_game_over())

    # JESSIE TEST CODE
