import random

def isWin(pos, goal_position): return (pos == goal_position)


def genRadPos(width, height, max_count):
    count = 0
    while count < max_count:
        yield random.randint(0, height - 1), random.randint(0, width - 1)
        count += 1


def isValidMove(position, width, height):
    x, y = position
    return 0 <= x < height and 0 <= y < width


def createBoard(width, height):
    return [['-' for _ in range(width)] for _ in range(height)]


def printBoardPreview(width, height, start_position, goal_position):
    board = createBoard(width, height)
    board[start_position[0]][start_position[1]] = 'A'
    board[goal_position[0]][goal_position[1]] = 'O'

    print("board generated")
    for row in board:
        print(' '.join(row))


def playGame(width, height, start_position, goal_position):

    board = createBoard(width, height)
    board[start_position[0]][start_position[1]] = 'A'
    board[goal_position[0]][goal_position[1]] = 'O'

    current_position = start_position
    while not isWin(current_position, goal_position):
        print("Current board:")
        for row in board:
            print(' '.join(row))

        move = input("What is your move [WASD]: ").lower()
        x, y = current_position
        if move == 'w':
            x -= 1
        elif move == 'a':
            y -= 1
        elif move == 's':
            x += 1
        elif move == 'd':
            y += 1

        new_position = (x, y)

        if isValidMove(new_position, width, height):
            board[current_position[0]][current_position[1]] = '-'
            board[new_position[0]][new_position[1]] = 'A'
            current_position = new_position
        else:
            print("Your move is not valid")

    print("You win!")


def mainMenu():
    print("~~ Selamat datang dipermainan board game pemrograman fungsional ~~")
    print("------------------------------------------------------------------")
    print("Anda (A) dapat berjalan secara horizontal dan vertikal untuk menuju target (O)\nGunakan keyboard WASD untuk bergerak")
    print("------------------------------------------------------------------")
    print("~~ Selamat bermain ~~")
    try:
        width = int(input("Enter the board width: "))
        height = int(input("Enter the board height: "))
        if width <= 0:
            raise ValueError("The width must be more than 0.")
        if height <= 0:
            raise ValueError("The height must be more than 0.")
    except ValueError:
        print("The value must be a number and more than 0")
        return

    for board_choice in range(0, 3):
        print(f"\nBoard choice {board_choice}:")
        gen_positions = genRadPos(width, height, 3)
        start_position = next(gen_positions)
        goal_position = next(gen_positions)

        printBoardPreview(width, height, start_position, goal_position)
        proceed = input(
            "New possition (Y/n): ").lower()
        if proceed != 'n':
            continue

        playGame(width, height, start_position, goal_position)
        break
    else:
        print("You lose")


if __name__ == "__main__":
    mainMenu()