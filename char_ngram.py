import tokenizer as tknzr
import angle as ang

cyrillic = "йцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ"


def preprocess_text(text):
    processed_text = ""
    for sentence in text:
        processed_sentence = preprocess_sentence(sentence)
        processed_text += processed_sentence
    return processed_text


def preprocess_sentence(sentence):
    processed_sentence = ""
    for token in sentence:
        for c in token:
            if c in cyrillic:
                if (c.lower() == 'ё'):
                    processed_sentence += 'е'
                else:
                    processed_sentence += c.lower()
    return processed_sentence


def build_vector(text):
    vector = [0] * (32 * 32)
    for i in range(0, len(text) - 1):
        c1 = text[i]
        c2 = text[i + 1]
        id1 = ord(c1) - ord('а')
        id2 = ord(c2) - ord('а')
        id = id1 * 32 + id2
        vector[id] += 1
    return vector


def get_vector(filename):
    text = tknzr.tokenize_file(filename)
    processed_text = preprocess_text(text)
    vector = build_vector(processed_text)
    return vector


def main():
    vec1 = get_vector("sample_input.txt")
    vec2 = get_vector("sample_input2.txt")
    print(ang.angle_between(vec1, vec2))
