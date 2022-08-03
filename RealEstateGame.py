# Author: Jessica Allman-LaPorte
# GitHub username: JessicaAllman-LaPorte
# Date: 7/28/2022
# Description:

import random


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
        self._space_owner_name = ""

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

    def set_space_owner(self, space_owner_name):
        """
        Sets owner name from default.
        Used by RealEstateGame class to set the space's owner.
        :param space_owner_name:
        :return:
        """
        self._space_owner_name = space_owner_name

    def get_space_owner(self):
        """
        Get method for owner name.
        Used by RealEstateGame class to get the space's owner.
        :return:
        """
        return self._space_owner_name

    def get_space_name(self):
        """returns name of space"""
        return self._space_name

    def set_space_name(self, space_name):
        """
        sets name of game space
        :param space_name:
        :return:
        """
        self._space_name = space_name


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
        Used by RealEstateGame class to set player position.
        :return:
        """
        self._player_position = new_position

    def move_player_position(self, spaces_to_move):
        """
        Used by RealEstateGame class to move player position.
        :return:
        """
        self._player_position += spaces_to_move

    def get_player_position(self):
        """
        Used by RealEstateGame class to get player position.
        :return: _player_position
        """
        return self._player_position

    def get_player_account_balance(self):
        """
        Used by RealEstateGame class to get player account balance.
        :return: _player_account_balance
        """
        return self._player_account_balance

    def update_player_account_balance(self, amount_change):
        """
        Used by RealEstateGame class to update player account balance.
        :param amount_change:
        """
        self._player_account_balance += amount_change


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
        self._spaces_list.append(GameSpace(pass_go_amount))
        self._spaces_list[0].set_purchase_price(None)  # sets go_space purchase price to None
        self._spaces_list[0].set_space_name('GO')

        # Creates exactly 24 more game spaces (for a total of 25):
        for space in range(1, 25):
            self._spaces_list.append(GameSpace(rent_amounts_array[space-1]))
            self._spaces_list[space].set_space_name("space_" + str(space))

    def create_player(self, player_name, player_account_balance):
        """
        Takes two parameters: a unique name and an initial account balance
        Purpose: To create a player object and add to player dictionary
        Players always start at the "GO" Space
        :param player_name
        :param player_account_balance:
        """
        self._player_dict[player_name] = Player(player_name, player_account_balance)

    def get_player_account_balance(self, player_name):
        """
        Takes as a parameter the name of the player and returns the player's account balance
        :param player_name
        :return: _player_account_balance
        """
        return self._player_dict[player_name].get_player_account_balance()

    def update_player_account_balance(self, player_name, amount_change):
        """
        Takes two parameters: player_name, amount_change
        Purpose: to update player's account balance.
        :param player_name:
        :param amount_change:
        :return:
        """
        self._player_dict[player_name].update_player_account_balance(amount_change)

    def get_player_current_position(self, player_name):
        """
        Takes as a parameter the name of the player and returns the player's current position
        on the board as an integer (where the "GO" space is position zero)
        :param player_name:
        :return: current_position
        """
        return self._player_dict[player_name].get_player_position()

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
        player_account_balance = self.get_player_account_balance(player_name)
        player_current_position = self.get_player_current_position(player_name)
        space_purchase_price = self._spaces_list[player_current_position].get_purchase_price()
        space_owner_name = self._spaces_list[player_current_position].get_space_owner()

        # TEST CODE:
        print(player_name, "account_balance:", player_account_balance)
        print("space purchase price:", space_purchase_price)

        # If player tries to purchase "GO" space, return False
        if space_purchase_price is None:
            print("Cannot purchase GO, continue turn")
            return False

        # If the space already has an owner, return false
        if space_owner_name != "":
            print("Space owned by", space_owner_name, ". Space cannot be purchased.")
            print()
            return False

        # If the player has an account balance greater than the purchase price:
        if player_account_balance > space_purchase_price:
            # The purchase price of the space will be deducted from the player's account
            self.update_player_account_balance(player_name, -space_purchase_price)

            # The player is set as the owner of the current space
            self._spaces_list[player_current_position].set_space_owner(player_name)

            # TEST CODE:
            print("Sufficient funds, space purchased")
            print("New account balance:", self.get_player_account_balance(player_name))
            print()
            return True

        else:
            # TEST CODE:
            print("Insufficient funds")

            return False

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

        player_account_balance = self.get_player_account_balance(player_name)
        player_current_position = self.get_player_current_position(player_name)
        pass_go_amount = self._spaces_list[0].get_rent_amount()

        # TEST CODE:
        print(player_name, "account balance:", player_account_balance)
        print(player_name, "current position:", player_current_position)
        print("# of spaces to move:", spaces_to_move)

        # If the player's account balance is 0, the method will return immediately without doing anything
        if player_account_balance == 0:
            print("Account zero, return\n")
            return

        player_current_position += spaces_to_move  # move

        # if player_current_position + spaces to move will make player pass or land on GO, player receives GO money
        #   and will subtract 25 to "loop" player in the game circle
        if player_current_position > 24:
            player_current_position -= 25
            self.update_player_account_balance(player_name, pass_go_amount)

        self._player_dict[player_name].set_player_position(player_current_position)
        # TEST CODE:
        print("new position:", player_current_position, "\n")

        # After the move is complete the player will pay rent for the new space occupied, if necessary
        space_rent = self._spaces_list[player_current_position].get_rent_amount()

        # if the player is occupying the "GO" space, the space has no owner, or the owner is the player:
        #     No rent will be paid
        if player_current_position == 0:
            return
        elif self._spaces_list[player_current_position].get_space_owner() == "":
            print("new position purchase price: " + str(space_rent * 5))
            print()
            return
        elif self._spaces_list[player_current_position].get_space_owner() == player_name:
            print("Already owned by " + player_name)
            print()
            return
        # Otherwise:
        #   The player must pay the rent for the space currently occupied
        else:
            space_owner = self._spaces_list[player_current_position].get_space_owner()
            self.update_player_account_balance(player_name, -space_rent)
            print("Owned by", space_owner, "pay", space_rent)
            self.update_player_account_balance(space_owner, space_rent)
            print()

        # The player will not pay more than the amount in player's account balance
        player_account_balance = self.get_player_account_balance(player_name)
        if player_account_balance < 0:
            self.update_player_account_balance(player_name, 0-player_account_balance)

        # The amount paid is deducted from the players account and deposited into the game space owner's account
        # If the player's new account balance is 0, the player has lost the game,
        #   and must be removed as the owner of any spaces
        if self.get_player_account_balance(player_name) == 0:
            for space in self._spaces_list:
                if space.get_space_owner() == player_name:
                    space.set_space_owner("")

    def check_game_over(self):
        """
        Takes no parameters.
        Purpose: To check for and declare game winner.
         - The game is over if all players but one have an account balance of 0
         - If the game is over, the method returns the winning player's name
         - Otherwise, the method returns an empty string
        :return: winning_player_name
        """
        players_out = 0
        winner = ""
        # Check for players with account balance 0
        for player in self._player_dict:
            if self.get_player_account_balance(player) == 0:
                players_out += 1
            else:
                winner = player

        if players_out == len(self._player_dict)-1:
            return winner
        else:
            return ""


def main():
    """Test code for RealEstateGame.py"""
    game = RealEstateGame()

    rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 250, 250, 300, 300, 300, 350,
             350, 350]
    game.create_spaces(200, rents)

    game.create_player("Jen", 2500)
    game.create_player("Jess", 2500)

    game.buy_space("Jen")
    game.move_player("Jen", 6)
    game.buy_space("Jen")

    game.move_player("Jess", 5)
    game.buy_space("Jess")

    game.move_player("Jen", 2)
    game.buy_space("Jen")

    game.move_player("Jess", 6)
    game.buy_space("Jess")

    game.move_player("Jen", 3)
    game.buy_space("Jen")
    game.move_player("Jess", 4)

    game.move_player("Jen", 2)
    game.buy_space("Jen")

    game.move_player("Jess", 2)

    game.move_player("Jen", 6)
    game.buy_space("Jen")
    game.buy_space("Jen")

    game.move_player("Jess", 3)

    game.move_player("Jen", 4)
    game.move_player("Jess", 5)

    game.move_player("Jen", 2)

    game.move_player("Jess", 1)
    game.buy_space("Jess")

    game.move_player("Jen", 6)
    game.move_player("Jess", 4)

    game.move_player("Jen", 2)

    game.move_player("Jess", 2)
    game.buy_space("Jess")

    game.move_player("Jen", 3)
    game.move_player("Jess", 2)

    game.move_player("Jen", 5)
    game.move_player("Jess", 2)

    game.move_player("Jen", 2)
    game.move_player("Jess", 1)

    game.move_player("Jen", 6)
    game.move_player("Jess", 1)

    game.move_player("Jen", 2)
    game.move_player("Jess", 4)

    game.move_player("Jen", 5)
    game.move_player("Jess", 6)

    game.move_player("Jen", 1)
    game.move_player("Jess", 2)

    game.move_player("Jen", 4)
    game.move_player("Jess", 5)

    game.move_player("Jen", 6)
    game.move_player("Jess", 1)

    game.move_player("Jen", 2)
    game.move_player("Jess", 1)

    game.move_player("Jen", 6)
    game.move_player("Jess", 2)
    game.buy_space("Jess")

    game.move_player("Jen", 4)
    game.buy_space("Jen")

    game.move_player("Jess", 3)

    game.move_player("Jen", 6)
    game.move_player("Jess", 6)
    for space in game._spaces_list:
        print(space._space_name + space.get_space_owner())

    print("Jen account balance:", game.get_player_account_balance("Jen"))
    print("Jess account balance:", game.get_player_account_balance("Jess"))

    print("Winner: " + game.check_game_over())
    print("Dice Roll:", random.randint(1, 6))


if __name__ == "__main__":
    main()
