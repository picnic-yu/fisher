def is_isbn_or_key(word):
    # isbn  isbn13 13个0到9的数字组成
    # isbn  isbn10 10个0到9的数字组成  含有一些-
    isbn_or_key = 'isbn_or_key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-','')
    if "-" in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key