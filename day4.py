import common


class Square:
    def __init__(self, square_number):
        self.number = square_number
        self.ticked = False

    def tick(self):
        self.ticked = True

    def untick(self):
        self.ticked = False

    def is_ticked(self):
        return self.ticked

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, board_number):
        self.rows = []
        self.board_number = board_number

    def add_row(self, column_numbers):
        squares = [Square(num) for num in column_numbers]
        self.rows.append(squares)

    def __tick_number(self, num):
        for row in self.rows:
            for square in row:
                if square.number == num:
                    square.tick()

    def check_number(self, num):
        self.__tick_number(num)
        # check the rows
        for row in self.rows:
            complete = True
            for square in row:
                if not square.is_ticked():
                    complete = False
                    break
            if complete:
                return True
        # check the columns
        for col in range(0, 5):
            complete = True
            for row in range(0, 5):
                square = self.rows[row][col]
                if not square.is_ticked():
                    complete = False
                    break
            if complete:
                return True
        # no complete row or column
        return False

    def unmarked_squares(self):
        return [square for square in common.flatmap(self.rows) if square.is_ticked() is False]

    def reset_squares(self):
        for row in self.rows:
            for square in row:
                square.untick()

    def __str__(self):
        mystr = ""
        for row in self.rows:
            mystr += str(row)
            mystr += '\n'
        return mystr


def build_boards(raw_data):
    board_num = 0
    all_boards = []
    current_board = None
    for i in range(1, len(raw_data)):
        line = raw_data[i]
        if line.strip().isspace() or line == "":
            if current_board is not None:
                all_boards.append(current_board)
            current_board = Board(board_num)
            board_num += 1
            continue
        # any line we read here goes towards the current board
        tokens = line.split(' ')
        current_board.add_row([int(token) for token in tokens if token != ""])
    return all_boards


def calculate_score(victory_board, number_just_called):
    return sum([square.number for square in victory_board.unmarked_squares()]) * number_just_called


data = common.read_all_data("input/day4.txt")
called_numbers = [int(num) for num in data[0].split(',')]
boards = build_boards(data)
print(f"First winner:")
for number in called_numbers:
    exit_loop = False
    for board in boards:
        victory = board.check_number(number)
        if victory:
            score = calculate_score(board, number)
            print(f"Board {board.board_number} wins!")
            print(f"{board}", end='')
            print(f"Unmarked numbers: {board.unmarked_squares()}")
            print(f"Score: {score}")
            exit_loop = True
            break
    if exit_loop:
        break
print(f"\nLast place:")
for board in boards:
    board.reset_squares()
for number in called_numbers:
    won = [board for board in boards if board.check_number(number) is True]
    boards = [board for board in boards if board not in won]
    if len(boards) == 0:
        board = won[0]
        print(f"Last place board: {board.board_number}")
        print(f"{board}", end='')
        print(f"Unmarked squares: {board.unmarked_squares()}")
        print(f"Score: {calculate_score(board, number)}")
        exit(0)
