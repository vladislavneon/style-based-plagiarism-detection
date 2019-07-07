import re


def tokenize(line):
    re.sub(r'. . .', '...', line)
    tokens = line.split()
    return tokens


def tokenize_file(filename):
    text = []
    with open(filename, 'r') as inf:
        for line in inf:
            text.append(tokenize(line))
    return text


def main():
    text = tokenize_file("sample_input.txt")
    print(text)
