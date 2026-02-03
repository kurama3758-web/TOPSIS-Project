# TOPSIS Project

This repository contains the implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using Python.

The project includes:
- Command Line Interface (CLI)
- Python Package (PyPI)
- Google Colab Notebook
- Web Service

---

## 1. Methodology

TOPSIS is a multi-criteria decision-making technique used to rank alternatives based on their distance from an ideal solution.

### Steps followed:
1. Construct the decision matrix
2. Normalize the decision matrix
3. Apply weights to normalized values
4. Determine ideal best and ideal worst solutions
5. Calculate separation measures
6. Compute TOPSIS score
7. Rank alternatives based on scores

---

## 2. Input Data

The input file contains:
- First column: Alternatives
- Remaining columns: Criteria values (numeric)

Example:
Model,Price,Mileage,Comfort,Safety
A,250000,20,7,8
B,300000,18,8,9
C,200000,22,6,7


---

## 3. Result Table

After applying TOPSIS, the following outputs are generated:
- **Topsis Score**: Relative closeness to the ideal solution
- **Rank**: Ranking of alternatives

The alternative with the highest TOPSIS score is ranked best.

---

## 4. Result Graph

A bar graph is plotted to visualize TOPSIS scores of different alternatives.
This graph helps in quick comparison and decision-making.

---

## 5. Google Colab Notebook

The complete TOPSIS implementation is available as a Google Colab notebook:

📓 `TOPSIS_Solution.ipynb`

The notebook demonstrates:
- Data upload
- TOPSIS computation
- Result table generation
- Result visualization

---

## 6. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab
- GitHub

---

## 7. Author

**Amogh Singh**

