import random


random.seed(0)

class Die():

    def rollDie(self):
        roll = random.randint(1, 6)
        return roll


class Player():

    plist = {'Player 1': 0, 'Player 2': 0}


class Game():

    def turn(self, player, t):
        turn_points = 0
        keep_rolling = True
        total = t
        print 'it is player {}s turn now'.format(player)
        raw_input('press enter to begin')
        while keep_rolling == True:
            rolled = Die().rollDie()
            print 'you rolled a {}'.format(rolled)
            if rolled == 1:
                print 'your game total is {}'.format(total)
                keep_rolling = False
            else:
                turn_points += rolled
                total += rolled
                print 'your rolling total is {}'.format(turn_points)
                print 'your game total is {}'.format(total)
                if total >= 100:
                    keep_rolling = False
                else:
                    y = raw_input('do you want to roll again (r)? or do you want to hold (h)')
                    if y == 'r':
                        keep_rolling = True
                    elif y == 'h':
                        keep_rolling = False
        print 'your turn is over'
        return turn_points


if __name__ == '__main__':

    print 'Welcome to the game PIG'
    winner = False
    while not winner:
        p_roll = Game().turn(1,  Player.plist['Player 1'])
        Player.plist['Player 1'] += p_roll
        print 'Player 1 point total is {}'.format(Player.plist['Player 1'])
        if Player.plist['Player 1'] >= 100:
            print 'Player 1 is the winner with {} points'.format(Player.plist['Player 1'])
            winner = True
        else:
            p_roll = Game().turn(2, Player.plist['Player 2'])
            Player.plist['Player 2'] += p_roll
            print 'Player 2 point total is {}'.format(Player.plist['Player 2'])
            if Player.plist['Player 2'] >= 100:
                print 'Player 2 is the winner with {} points'.format(Player.plist['Player 2'])
                winner = True
    print 'Goodbye Player'






