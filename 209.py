""" Created by Jieyi on 9/28/16. """


def rotated(pic):
    return [list(row) for row in zip(*reversed(pic))]


def is_match(window, pic_map, curr_x, curr_y):
    for k, v in pic_map.items():
        if k == 'head':
            continue
        for x, y in v:
            if window[curr_x + x][curr_y + y] != k:
                return False

    return True


def really_pic(pic):
    pic_map = {}
    for i in range(len(pic)):
        for j in range(len(pic[i])):
            if pic[i][j] != -1:
                if not pic_map.get('head'):
                    pic_map['head'] = (i, j)
                if pic_map.get(pic[i][j]):
                    pic_map[pic[i][j]].append((i, j))
                else:
                    pic_map[pic[i][j]] = [(i, j)]

    return pic_map


def start():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        window = [list(map(int, input().split())) for _ in range(m)]
        pic = [list(map(int, input().split())) for _ in range(n)]

        # print(pic)
        map0 = really_pic(pic)
        pic_rotated90 = rotated(pic)
        # print(pic_rotated90)
        map90 = really_pic(pic_rotated90)
        pic_rotated180 = rotated(pic_rotated90)
        # print(pic_rotated180)
        map180 = really_pic(pic_rotated180)
        pic_rotated270 = rotated(pic_rotated180)
        # print(pic_rotated270)
        map270 = really_pic(pic_rotated270)

        map_rotated = [map0, map90, map180, map270]

        res = algorithm(window, m, n, map_rotated)
        print(res if type(res) == str else str(res[0]) + ' ' + str(res[1]))


def algorithm(window, m, n, map_rotated):
    for map_ro in map_rotated:
        for i in range(m - n + 1):
            for j in range(m - n + 1):
                if is_match(window, map_ro, i, j):
                    return j + map_ro['head'][1] + 1, i + map_ro['head'][0] + 1
    return 'NA'


def main():
    start()


if __name__ == '__main__':
    main()
