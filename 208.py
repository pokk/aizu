""" Created by Jieyi on 9/20/16. """


def main():
    while True:
        num = int(input())
        if num == 0:
            break

        num = str(oct(num)[2:])
        ans = num.translate(str.maketrans('4567', '5789'))
        print(ans)


if __name__ == '__main__':
    main()
