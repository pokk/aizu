""" Created by Jieyi on 7/18/16. """

sample_input = '''
4
52 96 15 20
86 22 35 45
45 78 54 36
16 86 74 55
4
52 96 15 20
86 22 35 45
45 78 54 36
16 86 74 55
0
'''


def output_res(row):
    def five_fill_format(num):
        return '{:5}'.format(num)

    print(''.join(map(five_fill_format, row)), five_fill_format(sum(row)), sep='')
    # This two line is the same result, that's just difference writing.
    # print(''.join(map(lambda num: str(num).rjust(5), row)), str(sum(row)).rjust(5), sep='')


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        bottom_total = [0 for _ in range(n)]
        for _ in range(n):
            each_line = list(map(int, input().split()))
            output_res(each_line)
            bottom_total = [x + y for x, y in zip(bottom_total, each_line)]

        output_res(bottom_total)


if __name__ == '__main__':
    main()
