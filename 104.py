""" Created by Jieyi on 7/18/16. """

sample_input = '''
10 10
>>>v..>>>v
...v..^..v
>>>>>>^..v
.........v
.v<<<<...v
.v.v.^...v
.v.v.^<<<<
.v.v.....v
.v...^...v
.>>>>^....
6 10
>>>>>>>>>v
.........v
.........v
>>>>v....v
^...v....v
^<<<<<<<<<
0 0
'''


def run_magic_tiles(magic_tiles, past_matrix):
    i, j = 0, 0
    while True:
        move = {
            '^': (-1, 0),
            'v': (1, 0),
            '<': (0, -1),
            '>': (0, 1),
            '.': (-1, -1)
        }.get(magic_tiles[i][j])
        if move[0] == -1 and move[1] == -1:
            return j, i
        else:
            i += move[0]
            j += move[1]
            if past_matrix[i][j]:
                return 'LOOP'
            past_matrix[i][j] = 1


def main():
    while True:
        c, r = map(int, input().split())
        if c == 0 and r == 0:
            break

        past_matrix = [[0 for _ in range(r)] for _ in range(c)]
        tiles = []
        for _ in range(c):
            tiles.append(list(input()))

        res = run_magic_tiles(tiles, past_matrix)
        print('LOOP' if res == 'LOOP' else '%d %d' % (res[0], res[1]))


if __name__ == '__main__':
    main()
