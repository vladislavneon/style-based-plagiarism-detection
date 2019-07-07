import tokenizer as tknzr
import angle as ang

functional_words = ["и", "в", "не", "на",
                    "с", "что", "а", "по",
                    "к", "но", "как", "из",
                    "у", "за", "от", "о",
                    "для", "же", "только", "или",
                    "бы", "до", "если", "когда",
                    "вот", "при", "чтобы", "даже",
                    "во", "со", "под", "ну",
                    "после", "без", "ли", "то"]


def build_func_map():
    fm = {}
    cnt = 0
    for word in functional_words:
        fm[word] = cnt
        cnt += 1
    return fm


def preprocess_text(text):
    processed_text = []
    for sentence in text:
        processed_sentence = preprocess_sentence(sentence)
        processed_text += (processed_sentence)
    return processed_text


def preprocess_sentence(sentence):
    processed_sentence = []
    for token in sentence:
        if (token in functional_words):
            processed_sentence.append(token)
    return processed_sentence


def build_vector(text):
    vector = [0] * 36
    fm = build_func_map()
    for word in text:
        id = fm[word]
        vector[id] += 1
    return vector


def get_vector(filename):
    text = tknzr.tokenize_file(filename)
    processed_text = preprocess_text(text)
    vector = build_vector(processed_text)
    return vector


def main():
    vec1 = get_vector("sample_input.txt")
    print(vec1)
    vec2 = get_vector("sample_input2.txt")
    print(vec2)
    print(ang.angle_between(vec1, vec2))
