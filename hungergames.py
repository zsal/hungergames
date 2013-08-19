# Player: ZIGO - a hunger games player with a nasty attitude

class Player:
    def __init__(self):
        """
        Optional __init__ method is run once when your Player object is created before the
        game starts

        You can add other internal (instance) variables here at your discretion.

        """
        self.num_players = 0;
        self.percent_hunters = 0;
        self.my_hunt_percentage = .5;

    def hunt_choices(self, round_number, current_food, current_reputation, m,  player_reputations):
        # The main routine that plays each individual round.

        # You must create an array of variables 'hunt_decisions' and assign an 'h' for hunt or
        # an 's' for slack (i.e., not hunt) to each member of the array; the order of the hunt
        # decisions in hunt_decisions should correspond to the order of opponents'
        # reputations in player_reputations.

        # Blank variables or errors will be assigned 's'.

        # The variables passed in to hunt_choices for your use are:
        #     round_number: integer, the number round you are in.
        #     current_food: integer, the amount of food you have.
        #     current_reputation: float (python's representation of real numbers), your current reputation.
        #     m: integer, the threshold cooperation/hunting value for this round.
        #     player_reputations: list of floats, the reputations of all the remaining players in the game.
        #                         The ordinal positions of players in this list will be randomized each round.

        # - Strategy - 
        # slack with the hunters and hunt with the slackers
        # freeloader
        # non-punishing, non-random
        # educated 50 - 50 split that adjusts later based on number of hunters in the game
        # thinks that reputation is important so tries its best to maintain it while still survining

        self.num_players=len(player_reputations)

        odd_extra = 0
        if len(player_reputations) % 2:
            odd_extra = 1
        
        player_rep_map = sorted(range(len(player_reputations)), key=lambda k: player_reputations[k])
        shlist = ['h']*(int(len(player_reputations)*self.my_hunt_percentage) + odd_extra) + ['s']*int(len(player_reputations)*(1 - self.my_hunt_percentage))
        v = sorted(zip(player_rep_map,shlist))
        hunt_decisions = list(zip(*v)[1])

        return hunt_decisions


    def hunt_outcomes(self, food_earnings):
        # hunt_outcomes is called after all hunts for the round are complete.

        # Add any code you wish to modify your variables based on the outcome of the last round.

        # The variable passed in to hunt_outcomes for your use is:
        #     food_earnings: list of integers, the amount of food earned from the last round's hunts.
        #                    The entries can be negative as it is possible to lose food from a hunt.
        #                    The amount of food you have for the next round will be current_food
        #                    + sum of all entries of food_earnings + award from round_end.
        #                    The list will be in the same order as the decisions you made in that round.


        # - Strategy - 
        # Keep strategy simple, don't utilize this phase

        pass

    def round_end(self, award, m, number_hunters):
        # round_end is called after all hunts for the round are complete.

        # award - the total amount of food you received due to cooperation in the round.
        # Can be zero if the threshold m was not reached.

        # Add any code you wish to modify your variables based on the cooperation that occurred in
        # the last round.

        # The variables passed in to round_end for your use are:
        #     award: integer, total food bonus (can be zero) you received due to players cooperating
        #            during the last round. The amount of food you have for the next round will be
        #            current_food (including food_earnings from hunt_outcomes this round) + award.
        #     number_hunters: integer, number of times players chose to hunt in the last round.


        # - Strategy - 
        # Keeping reputation in mind, move 10% closer to number of hunters of current round in decisions for next round

        self.percent_hunters = float(number_hunters)/self.num_players;
        hunt_difference = self.percent_hunters - self.my_hunt_percentage;
        self.my_hunt_percentage += (.1 * hunt_difference);
