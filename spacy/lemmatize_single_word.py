import csv
from argparse import ArgumentParser

import chardet

import spacy
from preprocessing import is_token_allowed


def main(version, input_file_path):
    nlp = spacy.load("de_core_news_lg")
    with open(input_file_path, "rb") as f:
        encoding = chardet.detect(f.read())["encoding"]
    with open(input_file_path, "r", encoding=encoding) as f:
        text = f.read()
        words = text.split()

    with open(f"../results/spacy_single_word_{version}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["token", f"lemma single word {version}"])
        for word in words:
            doc = nlp(word)
            if is_token_allowed(
                doc[0], skip_punctuation=True, skip_one_letter_length=True
            ):
                writer.writerow([doc[0], doc[0].lemma_.lower()])


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", help="Spacy version", required=True)
    parser.add_argument("-i", "--input-file", help="Input file path", required=True)

    opt = parser.parse_args()

    main(opt.version, opt.input_file)
