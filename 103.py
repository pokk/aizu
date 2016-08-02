""" Created by Jieyi on 7/18/16. """

sample_input = '''
2
HIT
OUT
HOMERUN
HIT
HIT
HOMERUN
HIT
OUT
HIT
HIT
HIT
HIT
OUT
HIT
HIT
OUT
HIT
OUT
OUT
'''


def init_state():
    return 0, 0, 0


def main():
    n = int(input())

    point, hit, out = init_state()

    while True:
        if n == 0:
            break

        event = input()

        if event == 'HIT':
            if hit >= 3:
                point += 1
            else:
                hit += 1
        elif event == 'OUT':
            out += 1
        elif event == 'HOMERUN':
            point += hit + 1
            hit = 0

        if out == 3:
            print(point)
            point, hit, out = init_state()
            n -= 1


if __name__ == '__main__':
    main()
