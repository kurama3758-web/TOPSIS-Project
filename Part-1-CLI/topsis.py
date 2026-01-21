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
        if input_file.endswith(".csv"):
            df = pd.read_csv(input_file)
        elif input_file.endswith(".xlsx"):
            df = pd.read_excel(input_file)
        else:
            error("File must be .csv or .xlsx")
    except:
        error("Invalid file format")

    if df.shape[1] < 3:
        error("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]

    try:
        data = data.astype(float)
    except:
        error("From 2nd to last column must be numeric")

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        error("Number of weights, impacts and columns must be equal")

    for i in impacts:
        if i not in ["+", "-"]:
            error("Impacts must be + or -")

    # Normalize
    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm

    # Apply weights
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    s_plus = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_minus = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = s_minus / (s_plus + s_minus)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False)

    if output_file.endswith(".csv"):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print("Result saved to", output_file)

if __name__ == "__main__":
    main()
