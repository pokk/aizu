""" Created by Jieyi on 10/4/16. """
import io
import sys
import math

if len(sys.argv) > 1:
    filename = sys.argv[1]
    inp = ''.join(open(filename, "r").readlines())
    sys.stdin = io.StringIO(inp)


def lcm(x, y):
    return int((x * y) / math.gcd(x, y))


def mul_lcm(array):
    l = array[0]
    if len(array) > 1:
        for i in range(1, len(array)):
            l = lcm(array[i], l)

    return l


def algorithm(students, n):
    den = [students[i][1] for i in range(n)]  # speed
    denominator_lcm = mul_lcm(den)  # LCM(speed)
    print(den)

    # LCM(3, 4) = 12
    ans = [-1] * 20
    for i in range(n):
        ans[i] = students[i][0] * int(denominator_lcm / students[i][1])  # 
    print(ans)
    molecular_lcm = mul_lcm(ans[0:n])

    return [int(molecular_lcm / ans[i]) for i in range(n)]


def input_sample():
    while True:
        n = int(input())
        if n == 0:
            break

        students = [list(map(int, input().split(' '))) for _ in range(n)]
        answer_list = algorithm(students, n)

        for i in range(n):
            print(answer_list[i])


def main():
    input_sample()


if __name__ == '__main__':
    main()
