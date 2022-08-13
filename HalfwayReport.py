# Author: Jessica Allman-LaPorte
# GitHub username: JessicaAllman-LaPorte
# Date: 7/28/2022
# Description: Portfolio Project Halfway Report

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
1.	Determining how to store the board spaces and players
      -	Board spaces will be stored in a list (since they are numbered 0-24)
      -	Players will be stored in a dictionary
2.	Initializing the board spaces and players
      -	A player class will have data members storing the player’s name, account balance, and position.
      -	A game space class will have data members storing the space amount, space name, purchase price and
              space owner.
3.	Determining how to implement player piece movement
      -	Player position will be stored within player object
4.	Determining how to buy board spaces, and pay and receive rents
      -	Player will have the opportunity to purchase the space they land on after moving.
      -	If the player attempts to purchase a space, the method buy_space will check their account balance, whether
              it already has an owner, or whether they are on the go space.
      -	If they are able to purchase, the amount will be deducted from their account and the space object will
              store them as the owner.
      -	If a player moves and lands on a space owned by another player, the owner will receive the amount of rent,
              and the amount will be deducted from the players account
5.	Determining how to pass GO and receive the pay amount
      -	If the player’s current position + spaces to move will make player pass or land on GO (>25), player
              receives GO money and 25 will be subtracted to "loop" player in the game circle
6.	Determining when the game has ended
      -	The check_game_over method will check for players with account balance 0. When the amount of players – 1
              has a zero account balance, the game will end.
"""

class GameSpace(object):
    """
    A class to represents a game space the player can land on.
    Used by RealEstateGame class to create a game space.
    """
    def __init__(self, _space_amount):
        """
        Takes _space_amount as a parameter.
        The constructor for GameSpace class.
        Initializes the required data members.
        All data members are private.
        :param _space_amount:
        """
        pass

    def get_rent_amount(self):
        """
        Returns rent _space_amount.
        Used by RealEstateGame to get _space_amount (rent) that must be paid when
        non-owner player lands on space or the _space_amount paid to player
        when passing GO. _space_amount will be negative on go_space.
        """
        pass

    def get_purchase_price(self):
        """
        Returns purchase price.
        Used by RealEstateGame to get _space_amount that must be paid when
        non-owner player wishes to purchase the space.
        Default = rent _space_amount * 5
        """
        pass

    def set_purchase_price(self, purchase_price):
        """
        Sets purchase price from default.
        Used by RealEstateGame to set purchase price of GO to None.
        :param purchase_price:
        :return:
        """
        pass

    def set_space_owner(self, space_owner_name):
        """
        Sets owner name from default.
        Used by RealEstateGame class to set the space's owner.
        :param space_owner_name:
        :return:
        """
        pass

    def get_space_owner(self):
        """
        Get method for owner name.
        Used by RealEstateGame class to get the space's owner.
        :return: _space_owner_name
        """
        pass

    def get_space_name(self):
        """
        Get method for space name.
        Used by RealEstateGame class to get the space's name.
        self._space_name
        :return: _space_name
        """
        pass

    def set_space_name(self, space_name):
        """
        Sets name of game space
        Used by RealEstateGame class to set the space's name.
        :param space_name:
        :return:
        """
        pass


class Player(object):

    def __init__(self, player_name, player_account_balance):
        """
        The constructor for Player class.
        Initializes the required data members.
        All data members are private.
        """
        self._player_name = player_name
        self._player_account_balance = player_account_balance
        self._player_position = 0

    def set_player_position(self, new_position):
        """
        Takes new_position as a parameter.
        Used by RealEstateGame class to set player position.
        :return:
        """
        pass

    def move_player_position(self, spaces_to_move):
        """
        Takes spaces_to_move as a parameter.
        Used by RealEstateGame class to move player position.
        :return:
        """
        pass

    def get_player_position(self):
        """
        Used by RealEstateGame class to get player position.
        :return: _player_position
        """
        pass

    def get_player_account_balance(self):
        """
        Used by RealEstateGame class to get player account balance.
        :return: _player_account_balance
        """
        pass

    def update_player_account_balance(self, amount_change):
        """
        Used by RealEstateGame class to update player account balance.
        :param amount_change:
        """
        pass


class RealEstateGame(object):

    def __init__(self):
        """
        The constructor for RealEstateGame class.
        Initializes the required data members.
        All data members are private.
        """
        self._spaces_list = []
        self._player_dict = {}

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

        # Creates exactly 24 more game spaces (for a total of 25):
        pass

    def create_player(self, player_name, player_account_balance):
        """
        Takes two parameters: a unique name and an initial account balance
        Purpose: To create a player object and add to player dictionary
        Players always start at the "GO" Space
        :param player_name
        :param player_account_balance:
        """
        pass

    def get_player_account_balance(self, player_name):
        """
        Takes as a parameter the name of the player and returns the player's account balance
        :param player_name
        :return: _player_account_balance
        """
        pass

    def update_player_account_balance(self, player_name, amount_change):
        """
        Takes two parameters: player_name, amount_change
        Purpose: to update player's account balance.
        :param player_name:
        :param amount_change:
        :return:
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
        # If player tries to purchase "GO" space, return False

        # If the space already has an owner, return false

        # If the player has an account balance greater than the purchase price:
            # The purchase price of the space will be deducted from the player's account

            # The player is set as the owner of the current space

        # else:
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
        # If the player's account balance is 0, the method will return immediately without doing anything

        # if player_current_position + spaces to move will make player pass or land on GO, player receives GO money
        #   and will subtract 25 to "loop" player in the game circle

        # After the move is complete the player will pay rent for the new space occupied, if necessary

        # if the player is occupying the "GO" space, the space has no owner, or the owner is the player:
        #     No rent will be paid
        # Otherwise:
        #   The player must pay the rent for the space currently occupied

        # The player will not pay more than the amount in player's account balance

        # The amount paid is deducted from the players account and deposited into the game space owner's account
        # If the player's new account balance is 0, the player has lost the game,
        #   and must be removed as the owner of any spaces
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
        # Check for players with account balance 0
        pass
