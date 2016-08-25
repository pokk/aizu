""" Created by Jieyi on 8/16/16. """


def algorithm():
    def down_jump(x, y, times):
        if r == 1:
            return
        elif x == r:
            out_map[x - 1][y] += times
        elif x == r - 1:
            out_map[x][y] += times
        elif in_map[x][y] == 2:
            down_jump(x + 2, y, times)
        else:
            out_map[x][y] += times

    while True:
        c, r = map(int, input().split())
        if c == 0 and r == 0:
            break

        in_map = []
        out_map = [[0 for _ in range(c)] for _ in range(r)]
        for _ in range(r):
            in_map.append(list(map(int, input().split())))

        for i in range(c):
            if in_map[0][i] == 0 or in_map[0][i] == 2:
                out_map[0][i] = 1

        for i in range(r):
            for j in range(c):
                if in_map[i][j] == 0 or (i == 0 and in_map[i][j] == 2):
                    # ↙.
                    if i + 1 < r and j > 0 and in_map[i + 1][j - 1] == 0 and in_map[i][j] == 0:
                        out_map[i + 1][j - 1] += out_map[i][j]
                    # ↓.
                    if in_map[i][j] == 2:
                        down_jump(i, j, out_map[i][j])
                    elif i + 1 < r and in_map[i + 1][j] == 0:
                        out_map[i + 1][j] += out_map[i][j]
                    elif i + 1 < r and in_map[i + 1][j] == 2:
                        down_jump(i + 1, j, out_map[i][j])
                    # ↘.
                    if i + 1 < r and j + 1 < c and in_map[i + 1][j + 1] == 0 and in_map[i][j] == 0:
                        out_map[i + 1][j + 1] += out_map[i][j]

        for i in range(c):
            out_map[r - 1][i] = 0 if in_map[r - 1][i] and in_map[r - 2][i] != 2 else out_map[r - 1][i]
        print(sum(out_map[r - 1]))


def main():
    algorithm()


if __name__ == '__main__':
    main()
