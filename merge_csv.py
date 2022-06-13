import os

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

    token_dataframes = []
    for df in dataframes:
        token_dataframes.append(df.iloc[:, :1])
        df.drop(df.columns[0], axis=1, inplace=True)

    # assert all tokens have the same keywords
    for df in token_dataframes:
        assert df.columns.tolist() == token_dataframes[0].columns.tolist()

    tokens = token_dataframes[0]

    df = pd.concat(dataframes, axis=1)
    df = pd.concat([tokens, df], axis=1)

    df.to_csv("./results/merged.csv", index=False)


if __name__ == "__main__":
    main()
