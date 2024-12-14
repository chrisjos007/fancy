list_of_colors = [
    111122222,
    113422222,
    133444255,
    113422255,
    111222225,
    161178225,
    666778885,
    969578555,
    999555555,
]
k = 9

arr = [[int(i) for i in str(k)] for k in list_of_colors]
n = len(arr)
m = len(arr[0])

board = [[0 for _ in range(m)] for i in range(n)]
r1 = [0] * (k + 1)


def is_safe(row, col):
    """check if its safe to place the queen"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    if r1[arr[row][col]] == 1:
        return False

    if row > 0 and col > 0 and board[row - 1][col - 1] == 1:
        return False

    if row < n - 1 and col > 1 and board[row + 1][col - 1] == 1:
        return False

    if row > 0 and col < 1 and board[row - 1][col + 1] == 1:
        return False

    if row < n - 1 and col < m - 1 and board[row + 1][col + 1] == 1:
        return False

    return True


def solve(col):
    """for each column place in each cell and check if its possible to continue"""
    if col >= m:
        return True
    for i in range(n):
        if is_safe(i, col):

            board[i][col] = 1
            r1[arr[i][col]] = 1

            if solve(col + 1) is True:
                return True

            board[i][col] = 0
            r1[arr[i][col]] = 0
    return False


def print_sol():
    """prints the board"""
    print("\n" * 2)
    for i in range(n):
        for j in range(m):
            print(board[i][j], end=" ")
        print(end="\n")


if __name__ == "__main__":
    if solve(0) is False:
        print(False)
    print_sol()
