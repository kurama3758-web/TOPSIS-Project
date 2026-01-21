import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print("Error:", msg)
    sys.exit(1)

def main():
    if len(sys.argv) != 5:
        error("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")

    input_file, weights, impacts, output_file = sys.argv[1:]

    if not os.path.exists(input_file):
        error("Input file not found")

    try:
        df = pd.read_csv(input_file)
    except:
        error("Invalid file format")

    if df.shape[1] < 3:
        error("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:].values

    try:
        data = data.astype(float)
    except:
        error("From 2nd to last column must be numeric")

    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        error("Number of weights, impacts and columns must be equal")

    weights = np.array(weights, dtype=float)

    for i in impacts:
        if i not in ["+", "-"]:
            error("Impacts must be + or -")

    # Step 1: Normalize
    norm = np.sqrt((data ** 2).sum(axis=0))
    normalized = data / norm

    # Step 2: Weighted normalized
    weighted = normalized * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for j in range(len(impacts)):
        if impacts[j] == "+":
            ideal_best.append(weighted[:, j].max())
            ideal_worst.append(weighted[:, j].min())
        else:
            ideal_best.append(weighted[:, j].min())
            ideal_worst.append(weighted[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance
    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = s_minus / (s_plus + s_minus)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False)

    df.to_csv(output_file, index=False)
    print("Result saved to", output_file)

if __name__ == "__main__":
    main()
