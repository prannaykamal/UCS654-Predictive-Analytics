import sys
import os
import pandas as pd
import numpy as np

def error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

if len(sys.argv) != 5:
    error("Usage: $python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
file = sys.argv[1]
weights_inp = sys.argv[2]
impacts_inp = sys.argv[3]
out_file = sys.argv[4]

if not os.path.isfile(file):
    error("Input file not found")
try:
    df = pd.read_csv(file)
except Exception as e:
    error(f"Can't read input file: {e}")

if df.shape[1] < 3:
    error("Input file must contain more than 3 columns")

criteria = df.iloc[:, 1:].copy()
criteria = criteria.apply(pd.to_numeric, errors='coerce')
if criteria.isnull().values.any():
    error("Columns from 2 to end must contain numeric values only")

n_crit = criteria.shape[1]

weights_item = [w.strip() for w in weights_inp.split(',')]
if len(weights_item) != n_crit:
    error("Number of weights must match number of criteria columns")
try:
    weights = np.array([float(w) for w in weights_item], dtype=float)
except Exception:
    error("Weights must be numeric values separated by commas")

impacts_items = [s.strip() for s in impacts_inp.split(',')]
if len(impacts_items) != n_crit:
    error("Number of impacts must match number of criteria columns")

for im in impacts_items:
    if im not in ['+', '-']:
        error("Impacts must be either '+' or '-' and separated by commas")
impacts = impacts_items

col_norm = np.sqrt((criteria ** 2).sum(axis=0).astype(float))
if (col_norm == 0).any():
    error("At least one criterion column has zero norm (all zeros).")
    
norm = criteria / col_norm
weighted = norm * weights 

best = []
worst = []
for i in range(n_crit):
    col = weighted.iloc[:, i]
    if impacts[i] == '+':
        best.append(col.max())
        worst.append(col.min())
    else:
        best.append(col.min())
        worst.append(col.max())

best = np.array(best)
worst = np.array(worst)
best_dist = np.sqrt(((weighted - best) ** 2).sum(axis=1))
worst_dist = np.sqrt(((weighted - worst) ** 2).sum(axis=1))
denom = best_dist + worst_dist
scores = pd.Series(np.where(denom == 0, 0.0, worst_dist / denom), index=df.index)
ranks = scores.rank(ascending=False, method='dense').astype(int)
df['Topsis Score'] = scores.round(4)
df['Rank'] = ranks

try:
    df.to_csv(out_file, index=False)
except Exception as e:
    error(f"Can't write output file: {e}")

print("Done")