""" Created by Jieyi on 7/18/16. """

from sys import stdin

sample_input = '''
4
1001 2000 520
1002 1800 450
1003 1600 625
1001 200 1220
2
1001 100 3
1005 1000 100
2
2013 5000 100
2013 5000 100
0
'''


def main():
    for line in stdin:
        if int(line) == 0:
            break

        is_empty = True
        record = {}
        for _ in range(int(line)):
            employee = input().split()
            total = int(employee[1]) * int(employee[2])

            if total >= 1000000:
                print(employee[0])
                is_empty = False
            else:
                e_t = record.get(employee[0])

                if e_t:
                    e_t = record.get(employee[0]) + total
                    if e_t >= 1000000:
                        print(employee[0])
                        is_empty = False
                    else:
                        record[employee[0]] = e_t

                else:
                    record[employee[0]] = total

        record.clear()

        if is_empty:
            print('NA')


if __name__ == '__main__':
    main()
