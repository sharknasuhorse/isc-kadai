import time
import random
import curses

class CursesCtrl () :

    def __init__ (self):
        self.stdscr = curses.initscr()

    def print_curses(self, board):
        for row_index, i in enumerate(board):
            for col_index, j in enumerate(i):
                if j == True:
                    print("■", end="")
                    self.stdscr.addstr(row_index, col_index, "■")
                elif j == False:
                    self.stdscr.addstr(row_index, col_index, "□")
        self.stdscr.refresh()
        return

class Life_game():

    def borad_init(self, n):
        borad = []
        borad = [ [ random.choice([True, False]) for _ in range(n) ] for _ in range(n)]
        return borad 

    def exist_creature (self, borad, row, col):
        if borad[row][col] == True:
            return 1
        else:
            return 0

    def count (self, borad, check_row, check_col, n):
        true_count = 0
        if check_row - 1 >= 0 and check_col - 1 >= 0:
            true_count += self.exist_creature(borad, check_row - 1, check_col - 1)
        if check_row - 1 >= 0:
            true_count += self.exist_creature(borad, check_row - 1, check_col)
        if check_col - 1 >= 0 and check_col + 1 < n:
            true_count += self.exist_creature(borad, check_row - 1, check_col + 1)
        if check_col - 1 >= 0:
            true_count += self.exist_creature(borad, check_row, check_col - 1)
        if check_col + 1 < n:
            true_count += self.exist_creature(borad, check_row, check_col + 1)
        if check_row + 1 < n and check_col - 1 >= 0:
            true_count += self.exist_creature(borad, check_row + 1, check_col -1)
        if check_row + 1 < n:
            true_count += self.exist_creature(borad, check_row + 1, check_col)
        if check_row + 1 < n and check_col + 1 < n - 1:
            true_count += self.exist_creature(borad, check_row + 1, check_col + 1)
        return true_count
        
    def deadorlive(self, borad, check_row, check_col, n):
        true_count = self.count(borad, check_row, check_col, n)
        if true_count == 2 or true_count == 3:
            return True
        else:
            return False

    def born_creature(self, borad, check_row, check_col, n):
        true_count = self.count(borad, check_row, check_col, n)
        if true_count == 3:
            return True
        else:
            return False


if __name__ == "__main__":
    N = 30
    game = Life_game()
    start_borad = game.borad_init(N)
    current_borad = game.borad_init(N)
    cur = CursesCtrl()

    while True:
        for i in range(N):
            for j in range(N):
                if start_borad[i][j] == True:
                    current_borad[i][j] = game.deadorlive(start_borad, i, j, N)
                elif start_borad[i][j] == False:
                    current_borad[i][j] =  game.born_creature(start_borad, i, j, N)
        cur.print_curses(start_borad)
        time.sleep(0.1)
        start_borad = current_borad
