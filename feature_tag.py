__author__ = 'Hao'

from feature_table import FEATURE_TABLE


def get_tags(word):
    word = word.strip()
    tags = ""
    for f, tag in FEATURE_TABLE.items():
        if f(word):
            tags += tag + ","
    tags = "-1," if len(tags) == 0 else tags
    return tags[:-1]


def process_sentence(sentence):
    tag_list = []
    for word in sentence.split():
        tag_list.append([int(i) for i in get_tags(word).split(",")])
    return tag_list


def process_file(in_filename, out_filename):
    with open(out_filename, "w") as out_file:
        with open(in_filename, "r") as in_file:
            for line in in_file.read().splitlines():
                if len(line.strip()) > 0 and "-DOCSTART-" not in line:
                    out_file.write(get_tags(line.split()[0]) + "\n")


if __name__ == '__main__':
    test = "chicago, Pittsburgh abc 12 1992 ds2 32 2015 32 A8956-67 09-96 11/9/89 23,000.00 1.00 456789 BBN Sally can"
    temp = process_sentence(test)
    process_file("eng.train.txt", "hao.txt")