""" Created by Jieyi on 7/18/16. """

sample_input = '''
style 12
even 25
introduction 3
easy 9
style 7
document 13
style 21
even 18
'''


def main():
    book_index = {}
    while True:
        try:
            word, page = input().split(' ')
            page = int(page)
            if word in book_index:
                book_index[word].append(page)
            else:
                book_index[word] = [page]
        except Exception:
            break

    for k in sorted(book_index.keys()):
        print(k)
        print(' '.join(map(str, (sorted(book_index.get(k))))))


if __name__ == '__main__':
    main()
