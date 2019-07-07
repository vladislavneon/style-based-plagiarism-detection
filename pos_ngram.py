import pymorphy2
import tokenizer as tknzr
import angle as ang

morph = pymorphy2.MorphAnalyzer()

pos_tag_map = {"LATN": "UNKN",
               "PNCT": "UNKN",
               "NUMB": "NUMR",
               "intg": "NUMR",
               "real": "NUMR",
               "ROMN": "NUMR",
               "ADJF": "ADJ",
               "ADJS": "ADJ",
               "COMP": "ADJ",
               "INFN": "VERB",
               "PRTF": "PRT",
               "PRTS": "PRT",
               "NPRO": "NOUN",
               "PRED": "ADVB"}

main_pos = {"NOUN": 0,
            "ADJ": 1,
            "VERB": 2,
            "PRT": 3,
            "GRND": 4,
            "ADVB": 5}

extended_pos = {"NUMR": 0,
                "PREP": 1,
                "CONJ": 2,
                "PRCL": 3,
                "INTJ": 4}


def preprocess_text(text):
    processed_text = []
    for sentence in text:
        processed_sentence = preprocess_sentence(sentence)
        processed_text.append(processed_sentence)
    return processed_text


def preprocess_sentence(sentence):
    processed_sentence = []
    for token in sentence:
        parsed = morph.parse(token)[0]
        pos = parsed.tag.POS
        if (pos is not None):
            if (pos in pos_tag_map):
                processed_sentence.append(pos_tag_map[pos])
            else:
                processed_sentence.append(pos)
    return processed_sentence


def convert_text(text):
    converted_text = []
    for sentence in text:
        converted_sentence = convert_sentence(sentence)
        converted_text.append(converted_sentence)
    return converted_text


def convert_sentence(sentence):
    converted_sentence = []
    for pos in sentence:
        if (pos in main_pos):
            converted_sentence.append(pos)
    return converted_sentence


def build_vector(text, type="mixed"):
    n_mo = 0
    n_bi = 0
    if (type == "mixed"):
        vector = [0] * (6 * 6 + 11)
        for sentence in text:
            for pos in sentence:
                if (pos in main_pos):
                    id = main_pos[pos] + 5
                else:
                    id = extended_pos[pos]
                vector[id] += 1
                n_mo += 1
        text = convert_text(text)
        for sentence in text:
            for i in range(len(sentence) - 1):
                pos1 = sentence[i]
                pos2 = sentence[i + 1]
                id1 = main_pos[pos1]
                id2 = main_pos[pos2]
                id = id1 * 6 + id2 + 11
                vector[id] += 1
                n_bi += 1
        return vector
    elif (type == "bigram"):
        vector = [0] * (6 * 6)
        text = convert_text(text)
        for sentence in text:
            for i in range(len(sentence) - 1):
                pos1 = sentence[i]
                pos2 = sentence[i + 1]
                id1 = main_pos[pos1]
                id2 = main_pos[pos2]
                id = id1 * 6 + id2
                vector[id] += 1
        return vector


def get_vector(filename, type="mixed"):
    text = tknzr.tokenize_file(filename)
    processed_text = preprocess_text(text)
    vector = build_vector(processed_text, type=type)
    return vector


def main():
    text1 = tknzr.tokenize_file("sample_input.txt")
    processed_text1 = preprocess_text(text1)
    v11 = build_vector(processed_text1)
    v12 = build_vector(processed_text1, type="bigram")
    print(v11)
    print(v12)
    text2 = tknzr.tokenize_file("sample_input2.txt")
    processed_text2 = preprocess_text(text2)
    v21 = build_vector(processed_text2)
    v22 = build_vector(processed_text2, type="bigram")
    print(v21)
    print(v22)
    print(ang.angle_between(v11, v21))
    print(ang.angle_between(v12, v22))
