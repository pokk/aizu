""" Created by Jieyi on 7/2/16. """


def algorithm():
    def down_jump(x, y, times):
        if x == r:
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
        out_map = [[0 for _ in range(c)] for _ in range(r + 2)]

        # input
        in_map.append([0 for _ in range(c)])
        for _ in range(r):
            in_map.append(list(map(int, input().split())))
        in_map.append([0 for _ in range(c)])

        for i in range(r):
            if in_map[1][i] == 0 or in_map[1][i] == 2:
                out_map[1][i] = 1

        # for i in range(r):
        #     for j in range(c):
        #         if in_map[i][j] == 0:
        #             # ↙.
        #             if i + 1 < r and j > 0 and in_map[i + 1][j - 1] == 0:
        #                 out_map[i + 1][j - 1] += out_map[i][j]
        #             # ↓.
        #             if i + 1 < r and in_map[i + 1][j] == 0:
        #                 out_map[i + 1][j] += out_map[i][j]
        #             elif i + 1 < r and in_map[i + 1][j] == 2:
        #                 down_jump(i + 1, j, out_map[i][j])
        #             # ↘.
        #             if i + 1 < r and j + 1 < c and in_map[i + 1][j + 1] == 0:
        #                 out_map[i + 1][j + 1] += out_map[i][j]

        print(in_map)
        print(out_map)
        print(sum(out_map[c - 1]))


def main():
    algorithm()


if __name__ == '__main__':
    main()
