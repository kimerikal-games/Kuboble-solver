from collections import deque


def main():
    rows, cols, num_pieces = map(int, input().split())
    board = [input().strip() for _ in range(rows)]
    pieces = {}
    goals = {}
    for _ in range(num_pieces):
        piece_name, *others = input().split()
        py, px, gy, gx = map(int, others)
        pieces[piece_name] = (py, px)
        goals[piece_name] = (gy, gx)

    path = solve(board, pieces, goals)
    if path is None:
        print("Done: Unsolvable")
    else:
        for i, move in enumerate(path, 1):
            piece, direction = move
            print(i, piece, direction, sep="\t")
        print(f"Done: {len(path)} steps")


def solve(board, pieces, goals):
    search_queue = deque([(pieces, [])])
    visited = set([convert_to_state(pieces)])

    while search_queue:
        pieces, path = search_queue.popleft()
        if pieces == goals:
            return path
        for piece, pos in pieces.items():
            for direction in ["Up", "Down", "Left", "Right"]:
                new_pieces = pieces.copy()
                new_pieces[piece] = slide(board, pos, direction, new_pieces)
                new_state = convert_to_state(new_pieces)
                if new_state not in visited:
                    visited.add(new_state)
                    search_queue.append((new_pieces, path + [(piece, direction)]))

    return None


def slide(board, pos, direction, pieces):
    direction_map = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    dy, dx = direction_map[direction]
    y, x = pos

    while True:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < len(board) and 0 <= nx < len(board[0])):
            break
        if board[ny][nx] == "#":
            break
        if (ny, nx) in pieces.values():
            break
        y, x = ny, nx

    return y, x


def convert_to_state(pieces):
    return tuple(sorted(pieces.items()))


if __name__ == "__main__":
    main()
