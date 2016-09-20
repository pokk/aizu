""" Created by Jieyi on 9/6/16. """


def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    s = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = int((m * m - 3) / 2)
            s[j] = 0
            while j < half:
                if j >= len(s):
                    j += m
                    continue
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]


prime = primes(1000000)


def mark_array(index, arr_list, price_list):
    for t in price_list:
        if index + t < len(arr_list):
            arr_list[index + t] = 1


def algorithm():
    while True:
        n, total = map(int, input().split())
        if n == 0 and total == 0:
            break

        price = []
        arr_list = [0 for _ in range(total + 1)]

        for i in range(n):
            price.append(int(input()))

        for i in range(len(arr_list)):
            for p in price:
                if arr_list[i] == 0 and i % p == 0:
                    arr_list[i] = 1
                    mark_array(i, arr_list, price)
                elif arr_list[i] == 1:
                    mark_array(i, arr_list, price)

        if all(arr_list):
            print('NA')
        else:
            for i in range(total, -1, -1):
                if arr_list[i] == 1:
                    if i in prime:
                        print(i)
                        break
                if i == 0:
                    print('NA')


def main():
    algorithm()


if __name__ == '__main__':
    main()
