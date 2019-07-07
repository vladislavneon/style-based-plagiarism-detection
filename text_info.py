import tokenizer as tknzr
import string
import sys


def is_punct(s):
    for c in s:
        if (c not in string.punctuation):
            return False
    return True


def get_vector(filename):
    t = get_info(filename)
    vec = [t[3], t[5]]
    return vec


def get_info(filename):
    text = tknzr.tokenize_file(filename)
    cnt_sent = len(text)
    cnt_words = 0
    cnt_symbols = 0
    cnt_words_len = 0
    for sentence in text:
        for token in sentence:
            cnt_symbols += len(token)
            if (not is_punct(token)):
                cnt_words += 1
                cnt_words_len += len(token)
    print("{0}\nsentences: {1}\nwords: {2}\nsymbols: {3}\naverage words in sentence: {4}\naverage symbols in sentence: {5}\naverage word length: {6}\n".format(filename, cnt_sent, cnt_words, cnt_symbols, cnt_words / cnt_sent, cnt_symbols / cnt_sent, cnt_words_len / cnt_words))
    return (cnt_sent, cnt_words, cnt_symbols, (cnt_words / cnt_sent), (cnt_symbols / cnt_sent), (cnt_words_len / cnt_words))


def main():
    args = sys.argv
    if (len(args) == 3):
        folder = args[1]
        file = args[2]
        path = "{}\{}".format(folder, file)
    else:
        file = args[1]
        path = "{}".format(file)
    get_info(path)


main()
