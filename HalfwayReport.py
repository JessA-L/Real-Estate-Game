# Author: Jessica Allman-LaPorte
# GitHub username: JessicaAllman-LaPorte
# Date: 7/28/2022
# Description:

class GameSpace(object):
    """
    A class to represents a game space the player can land on.
    Used by RealEstateGame class.
    """
    def __init__(self, _space_amount):
        """
        The constructor for GameSpace class.
        Initializes the required data members.
        All data members are private.
        :param _space_amount:
        """
        self._space_amount = _space_amount
        self._space_name = ""
        self._purchase_price = _space_amount * 5

    def get_rent_amount(self):
        """
        Returns rent _space_amount.
        Used by RealEstateGame to get _space_amount (rent) that must be paid when
        non-owner player lands on space or the _space_amount paid to player
        when passing GO. _space_amount will be negative on go_space.
        """
        return self._space_amount

    def get_purchase_price(self):
        """
        Returns purchase price.
        Used by RealEstateGame to get _space_amount that must be paid when
        non-owner player wishes to purchase the space.
        Default = rent _space_amount * 5
        """
        return self._purchase_price

    def set_purchase_price(self, purchase_price):
        """
        Sets purchase price from default.
        Used by RealEstateGame to set purchase price of GO to None.
        :param purchase_price:
        :return:
        """
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


class Player(object):

    def __init__(self):
        """
        The constructor for Player class.
        Initializes the required data members.
        All data members are private.
        """
        pass


class RealEstateGame(object):

    # create_spaces -
    def __init__(self):
        """
        The constructor for RealEstateGame class.
        Initializes the required data members.
        All data members are private.
        """
        self._spaces_dict = {}

    def create_spaces(self, pass_go_amount, rent_amounts_array):
        """
        Takes two parameters: the _space_amount of money given to players when they
            land on or pass the "GO" space, and an array of 24 integers (rent amounts)
        Purpose: Creates game spaces and assigns rent to space
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
            # Each space will have a purchase price equal to 5 times the rent _space_amount

        for i in range(24):
            self._spaces_dict['space_' + str(i+1)] = GameSpace(rent_amounts_array[i])
        print(self._spaces_dict)


    def create_player(self, player_name, player_account_balance):
        """
        Takes two parameters: a unique name and an initial account balance
        Players always start at the "GO" Space
        """
        pass

    def get_player_account_balance(self, player_name):
        """
        Takes as a parameter the name of the player and
        returns the player's account balance
        :param player_name
        :return: player_account_balance
        """
        pass


    def get_player_current_position(self, player_name):
        """
        Takes as a parameter the name of the player and returns the player's current position
        on the board as an integer (where the "GO" space is position zero)
        :param player_name:
        :return: current_position
        """
        pass


    def buy_space(self, player_name):
        """
        Takes as parameters the name of the player
        Purpose: When a player lands on a space, this method can be used to purchase the space
        - If the player has an account balance greater than the purchase price, 
            and the space doesn't already have an owner:
            - The purchase price of the space will be deducted from the player's account
            - The player is set as the owner of the current space
            - The method returns True
        - Otherwise, the method returns False
        :param player_name: 
        :return: True or False
        """
        pass
        

    def move_player(self, player_name, spaces_to_move):
        """
        Takes as parameters the name of the player, and the number of spaces to move
        Purpose: To check a player's ability to advance spaces
                 To advance the player around the circular board by the number of spaces (1-6 spaces).
                 To charge player rent if necessary and to pay player for passing "GO"
        :param player_name:
        :param spaces_to_move:
        :return:
        """
        pass


    def check_game_over(self):
        """
        Takes no parameters.
        Purpose: To check for and declare game winner.
         - The game is over if all players but one have an account balance of 0
         - If the game is over, the method returns the winning player's name
         - Otherwise, the method returns an empty string
        :return: winning_player_name
        """
        pass


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
