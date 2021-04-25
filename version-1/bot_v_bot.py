from __future__ import print_function
# tag::bot_vs_bot[]
from algo import agent
from algo import goboard_slow as goboard
from algo import gotypes
from algo.utils import print_board, print_move, clear_screen
import time


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }

        clear_screen()   
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()

# end::bot_vs_bot[]