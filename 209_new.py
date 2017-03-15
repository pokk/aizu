""" Created by Jieyi on 10/9/16. """
import io
import sys

# Simulate the redirect stdin.
if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)


def print_map(window):
    for i in range(len(window)):
        print(window[i])


def rotated(pic):
    return [list(row) for row in zip(*reversed(pic))]


def input_source():
    while True:
        m, n = map(int, input().split())
        if m == 0 and n == 0:
            break

        window = [list(map(int, input().split())) for _ in range(m)]
        pic = [list(map(int, input().split())) for _ in range(n)]

        res = algorithm(m, n, window, pic)
        print(res if type(res) == str else str(res[0]) + ' ' + str(res[1]))


def match(start_x, start_y, window, fragment):
    for h in range(len(fragment)):
        for w in range(len(fragment[h])):
            if fragment[h][w] == -1:
                continue
            if fragment[h][w] != window[start_x + h][start_y + w]:
                return False
    return True


def algorithm(m, n, window, fragment):
    origin = fragment
    rotated_270 = rotated(origin)
    rotated_180 = rotated(rotated_270)
    rotated_90 = rotated(rotated_180)

    array = [origin, rotated_90, rotated_180, rotated_270]

    for pic in array:
        for h in range(m - n + 1):
            for w in range(m - n + 1):
                if match(h, w, window, pic):
                    for h_p in range(len(pic)):
                        for w_p in range(len(pic[h_p])):
                            if pic[h_p][w_p] != -1:
                                return w + w_p + 1, h + h_p + 1
    return 'NA'


def main():
    input_source()


if __name__ == '__main__':
    main()
