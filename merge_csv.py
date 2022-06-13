import os
from functools import reduce

import chardet
import pandas as pd


def main():
    filenames = [
        f"./results/{filename}"
        for filename in os.listdir("./results")
        if filename.startswith("spacy_")
        and filename.endswith(".csv")
        and filename != "merged.csv"
    ]

    dataframes = []
    for filename in filenames:
        with open(filename, "rb") as f:
            encoding = chardet.detect(f.read())["encoding"]
        dataframes.append(pd.read_csv(filename, encoding=encoding))

    # merge dataframes
    merged = reduce(
        lambda left, right: pd.merge(left, right, on="token", how="outer"), dataframes
    ).drop_duplicates()

    merged.to_csv("./results/merged.csv", index=False)


if __name__ == "__main__":
    main()
