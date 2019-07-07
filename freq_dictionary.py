import pymorphy2
import tokenizer as tknzr
import csv
import statistics

morph = pymorphy2.MorphAnalyzer()
ignorable_grammemes = set(["LATN", "PNCT", "NUMB", "intg", "real", "ROMN", "UNKN", "NUMR", "NPRO", "PREP", "CONJ", "PRCL", "INTJ"])
functional_grammemes = set(["PREP", "CONJ", "PRCL", "INTJ"])


def preprocess_text(text, type="all"):
    if (type == "all" or type == "func"):
        processed_text = []
        for sentence in text:
            processed_sentence = preprocess_sentence(sentence, type=type)
            processed_text += processed_sentence
        return processed_text
    elif (type == "unique"):
        processed_text = set()
        for sentence in text:
            processed_sentence = preprocess_sentence(sentence, type="unique")
            processed_text |= processed_sentence
        return processed_text


def preprocess_sentence(sentence, type="unique"):
    if (type == "all"):
        processed_sentence = []
        for token in sentence:
            parsed = morph.parse(token)[0]
            norm = parsed.normal_form
            if ((parsed.tag.POS != None) and (parsed.tag.POS not in ignorable_grammemes)):
                processed_sentence.append(norm)
        return processed_sentence
    elif (type == "unique"):
        processed_sentence = set()
        for token in sentence:
            parsed = morph.parse(token)[0]
            norm = parsed.normal_form
            if ((parsed.tag.POS != None) and (parsed.tag.POS not in ignorable_grammemes)):
                processed_sentence.add(norm)
        return processed_sentence
    elif (type == "func"):
        processed_sentence = []
        for token in sentence:
            parsed = morph.parse(token)[0]
            norm = parsed.normal_form
            if ((parsed.tag.POS != None) and (parsed.tag.POS in functional_grammemes)):
                processed_sentence.append(norm)
        return processed_sentence


def load_freq_dictionary():
    freq_dictionary = {}
    with open("freqrnc2012.csv", newline='') as inf:
        inf.readline()
        fd = csv.reader(inf, delimiter='    ')
        for row in fd:
            lemma = row[0]
            freq = float(row[2])
            if (lemma in freq_dictionary):
                freq_dictionary[lemma] = max(freq, freq_dictionary[lemma])
            else:
                freq_dictionary[lemma] = freq
    return freq_dictionary


def count_freq(text, fd, threshold=1000.0, method="arithm"):
    freqs = []
    for word in text:
        if (word in fd):
            if (fd[word] <= threshold):
                freqs.append(fd[word])
            else:
                freqs.append(threshold)
    if (method == "arithm"):
        return statistics.mean(freqs)
    elif (method == "harm"):
        return statistics.harmonic_mean(freqs)


def get_freq(filename, threshold=1000):
    text = tknzr.tokenize_file(filename)
    processed_text = preprocess_text(text)
    res = count_freq(processed_text, fd, threshold)
    return res


def main():
    af1 = get_freq("simple_text_1_1.txt")
    print(af1)
    af2 = get_freq("simple_text_1_2.txt")
    print(af2)


fd = load_freq_dictionary()
