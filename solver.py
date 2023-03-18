from collections import deque


class Solver:
    __slots__ = ("board", "pieces", "goals")

    def __init__(self, board: list[str], pieces: dict[str, tuple[int, int]], goals: dict[str, tuple[int, int]]):
        self.board = board
        self.pieces = pieces
        self.goals = goals

    def _as_state(self, pieces: dict[str, tuple[int, int]]) -> tuple[tuple[str, tuple[int, int]]]:
        return tuple(sorted(pieces.items()))

    def solve(self):
        jobs = deque([(self.pieces, list[str]())])
        visited = set([self._as_state(self.pieces)])

        while jobs:
            pieces, path = jobs.popleft()
            if pieces == self.goals:
                return path
            for piece, (y, x) in pieces.items():
                for direction in "UDLR":
                    new_pieces = pieces.copy()
                    new_pieces[piece] = self._move(y, x, direction, new_pieces)
                    new_state = self._as_state(new_pieces)
                    if new_state not in visited:
                        visited.add(new_state)
                        jobs.append((new_pieces, path + [piece + direction]))

        return None

    def _move(self, y: int, x: int, direction: str, pieces: dict[str, tuple[int, int]]) -> tuple[int, int]:
        direction_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        dy, dx = direction_map[direction]

        while True:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < len(self.board) and 0 <= nx < len(self.board[0])):
                break
            if self.board[ny][nx] == "#":
                break
            if (ny, nx) in pieces.values():
                break
            y, x = ny, nx

        return y, x


piece_map = {"W": "White", "K": "Black", "O": "Orange", "G": "Green"}
direction_map = {"U": "Up", "D": "Down", "L": "Left", "R": "Right"}

if __name__ == "__main__":
    board = [
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
        "........",
    ]
    pieces = {
        "A": (0, 0),
        "B": (0, 1),
        "C": (0, 2),
        "D": (0, 3),
    }
    goals = {
        "A": (3, 2),
        "B": (5, 0),
        "C": (6, 7),
        "D": (3, 6),
    }
    solver = Solver(board, pieces, goals)
    solution = solver.solve()

    if solution is None:
        print("No solution")
    else:
        print(f"Can be solved in {len(solution)} moves.")
        for move in solution:
            piece, direction = move
            piece = piece_map.get(piece, piece)
            direction = direction_map[direction]
            print(f"Move {piece} piece {direction}.")
