""" Created by Jieyi on 7/18/16. """

sample_input = '''
3
Hoshino
Hashino
Masayuki Hoshino was the grandson of Ieyasu Tokugawa.
'''


def main():
    n = input()
    for line in range(int(n)):
        print(input().replace('Hoshino', 'Hoshina'))


if __name__ == '__main__':
    main()
