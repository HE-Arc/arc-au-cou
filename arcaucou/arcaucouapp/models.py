from django.db import models
from django.contrib.auth.models import User
import random
import copy
import datetime
import json
import numpy as np

# Create your models here.


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Date is added automatically
    date = models.DateField(auto_now_add=True)
    # Time in milliseconds
    time = models.DecimalField(max_digits=10, decimal_places=0)


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


class UserToGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Sudoku(models.Model):
    """
    Tutoriel followed : https://medium.com/codex/building-a-sudoku-solver-and-generator-in-python-1-3-f29d3ede6b23
    How to generate and solve a sudoku
    """
    start_sudoku = models.TextField()
    end_sudoku = models.TextField()
    date = models.DateField()

    def generate(self):
        """
        Generate the sudoku and its solution
        """
        self.start_sudoku, self.end_sudoku = self.generate_sudoku(
            self.__generate_random_complete_board())
        self.date = datetime.datetime.now()

    def format(self):
        """
        Format the sudoku so each array in the 2d array represent a square of the sudoku
        """
        # Get the current sudoku and get it in a list
        current_board = json.loads(self.start_sudoku)
        # The sudoku in a formated form
        formated_sudoku = []
        # Temporary list which will contain a line of the sudoku
        line = []
        # Temporary lists which will contain the squares of the sudoku
        first_square = []
        second_square = []
        third_square = []

        for row in range(9):
            for col in range(9):
                # Get the line of the sudoku
                line.append(current_board[row][col])

            # Split it in 3 squares
            # First square - leftmost
            first_square.append(line[0])
            first_square.append(line[1])
            first_square.append(line[2])
            # Second square - center
            second_square.append(line[3])
            second_square.append(line[4])
            second_square.append(line[5])
            # Third square - rightmost
            third_square.append(line[6])
            third_square.append(line[7])
            third_square.append(line[8])
            # Empty the temporary list
            line.clear()
            # Each 3 lines, we add the squares to the formated sudoku and empty the squares lists
            if (row + 1) % 3 == 0:
                formated_sudoku.append(copy.deepcopy(first_square))
                formated_sudoku.append(copy.deepcopy(second_square))
                formated_sudoku.append(copy.deepcopy(third_square))
                first_square.clear()
                second_square.clear()
                third_square.clear()

        return formated_sudoku

    def check_win(self, board):
        """
        Check if the user has completed the sudoku correctly
        """
        current_board = json.loads(board)
        end_board = self.format(json.loads(self.end_sudoku))
        return np.all(np.asarray(current_board) == np.asarray(end_board))

    def init_sudoku(self, code=None):
        """
        Fill the sudoku with a string code
        """
        self.reset_sudoku()
        self.code_to_board(code)

    def reset_sudoku(self):
        """
        Reset the sudoku board to 0
        """
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        return self.board

    def board_to_code(self, input_board=None):
        """
        Transform a sudoku into a string code
        """
        if input_board:
            _code = ''.join([str(i) for j in input_board for i in j])
            return _code
        else:
            self.code = ''.join([str(i) for j in self.board for i in j])
            return self.code

    def code_to_board(self, code=None):
        """
        Transform a code into a sudoku board
        """
        if code:
            self.code = code

            for row in range(9):
                for col in range(9):
                    self.board[row][col] = int(code[0])
                    code = code[1:]
        else:
            self.code = None

# region Generate
    def __find_spaces_to_find_number_of_solutions(self, board, h):
        k = 1
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 0:
                    if k == h:
                        return (row, col)

                    k += 1

        return False

    def __solve_to_find_number_of_solutions(self, row, col):
        """
        Solves the board using recursion
        """
        for n in range(1, 10):
            if self.check_space(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False

    def __generate_cont(self):
        """
        Uses recursion to finish generating a random board
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    num = random.randint(1, 9)

                    if self.check_space(num, (row, col)):
                        self.board[row][col] = num

                        if self.solve():
                            self.__generate_cont()
                            return self.board

                        self.board[row][col] = 0

        return False

    def __generate_random_complete_board(self):
        """
        Generates a brand new completely random board full of numbers
        """
        # Reset the sudoku
        self.reset_sudoku()

        # Fill the diagonal independent boxes
        # Top leftmost box
        l = list(range(1, 10))
        for row in range(3):
            for col in range(3):
                num = random.choice(l)
                self.board[row][col] = num
                l.remove(num)

        # Center box
        l = list(range(1, 10))
        for row in range(3, 6):
            for col in range(3, 6):
                num = random.choice(l)
                self.board[row][col] = num
                l.remove(num)

        # Bottom rightmost box
        l = list(range(1, 10))
        for row in range(6, 9):
            for col in range(6, 9):
                num = random.choice(l)
                self.board[row][col] = num
                l.remove(num)

        return self.__generate_cont()

    def find_number_of_solutions(self):
        """
        Finds the number of solutions to a board and returns the list of solutions
        """

        z = 0
        solutions_list = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    z += 1

        for i in range(1, z + 1):
            _board_copy = copy.deepcopy(self)

            _row, _col = self.__find_spaces_to_find_number_of_solutions(
                _board_copy.board, i)
            _board_copy_solution = _board_copy.__solve_to_find_number_of_solutions(
                _row, _col)

            solutions_list.append(self.board_to_code(_board_copy_solution))

        return list(set(solutions_list))

    def generate_sudoku(self, full_board):
        """
        Generate the starting sudoku from the full sudoku
        """
        self.board = copy.deepcopy(full_board)

        # Easy mode
        _squares_to_remove = 36

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(0, 2)
            _rCol = random.randint(0, 2)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(3, 5)
            _rCol = random.randint(3, 5)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _counter = 0
        while _counter < 4:
            _rRow = random.randint(6, 8)
            _rCol = random.randint(6, 8)
            if self.board[_rRow][_rCol] != 0:
                self.board[_rRow][_rCol] = 0
                _counter += 1

        _squares_to_remove -= 12
        _counter = 0
        while _counter < _squares_to_remove:
            _row = random.randint(0, 8)
            _col = random.randint(0, 8)

            if self.board[_row][_col] != 0:
                n = self.board[_row][_col]
                self.board[_row][_col] = 0

                if len(self.find_number_of_solutions()) != 1:
                    self.board[_row][_col] = n
                    continue

                _counter += 1

        return json.dumps(self.board), json.dumps(full_board)
# endregion

# region Solve
    # Solve
    def solution_code(self):
        """
        Return the sudoku code of the solution
        """
        return self.board_to_code(self.solve())

    def find_empty_cell(self):
        """
        Find the first empty cell in the sudoku, the first cell containing 0
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)

        return False

    def check_space(self, num, space):
        """
        Check to see if a number can be fitted into a specific space (Square, row, col)
        """
        # Check if the cell is already occupied
        if self.board[space[0]][space[1]] != 0:
            return False

        # Check if the col is already containing the number
        for col in self.board[space[0]]:
            if col == num:
                return False

        # Check if the row is already containing the number
        for row in range(len(self.board)):
            if self.board[row][space[1]] == num:
                return False

        # Check if the square is already containing the number
        internal_box_row = space[0] // 3
        internal_bow_col = space[1] // 3

        for i in range(3):
            for j in range(3):
                if self.board[i + (internal_box_row * 3)][j + (internal_bow_col * 3)] == num:
                    return False

        # Otherwise return true
        return True

    def solve(self):
        """
        Function used to solve the sudoku, using recursion
        """
        spaces_available = self.find_empty_cell()

        if not spaces_available:
            return True
        else:
            row, col = spaces_available

        for n in range(1, 10):  # range [1-9]
            if self.check_space(n, (row, col)):
                self.board[row][col] = n

                if self.solve():
                    return self.board

                self.board[row][col] = 0

        return False

    # endregion
