import csv
from pathlib import Path


def main():
    levelpath = Path("levels")
    levelpath.mkdir(exist_ok=True)

    with open("featured.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            num_pieces, level, num_moves, board, pieces, goals = parse_row(row)
            level_str = format_level(num_pieces, level, num_moves, board, pieces, goals)
            with open(levelpath / f"{level}.txt", "w") as g:
                g.write(level_str)


def parse_row(row):
    num_pieces = int(row[1].split()[0])
    level = int(row[2].split()[1])
    num_moves = int(row[3])
    board = []
    pieces = {}
    goals = {}
    board_str = row[4]
    for i, row_str in enumerate(board_str.split(";")):
        row = []
        for j in range(0, len(row_str) // 2):
            c = row_str[2 * j]
            d = row_str[2 * j + 1]

            if c == "X" or d == "X":
                row.append("#")
                continue

            row.append(".")

            if c.isalpha():
                if c.islower():
                    goals[c.upper()] = (i, j)
                elif c.isupper():
                    pieces[c] = (i, j)

            if d.isalpha():
                if d.islower():
                    goals[d.upper()] = (i, j)
                elif d.isupper():
                    pieces[d] = (i, j)

        board.append(row)

    # sanity check
    assert num_pieces == len(pieces) == len(goals)
    assert pieces.keys() == goals.keys()

    return num_pieces, level, num_moves, board, pieces, goals


def format_level(num_pieces, level, num_moves, board, pieces, goals):
    board_str = "\n".join("".join(row) for row in board)
    piece_str = "\n".join(
        f"{piece} {pieces[piece][0]} {pieces[piece][1]} {goals[piece][0]} {goals[piece][1]}"
        for piece in sorted(pieces)
    )
    return f"{len(board)} {len(board[0])} {num_pieces}\n{board_str}\n{piece_str}\n"


main()
