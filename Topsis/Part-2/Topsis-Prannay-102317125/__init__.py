import sys
import os
import pandas as pd
import numpy as np

def validate_inputs(inp_file, weights_str, impacts_str):
    if not os.path.isfile(inp_file):
        raise FileNotFoundError("Input file not found.")

    try:
        df = pd.read_csv(inp_file)
    except Exception as e:
        raise Exception(f"Can't read input file: {e}")

    if df.shape[1] < 3:
        raise ValueError("Input file must contain more than 2 columns")

    criteria = df.iloc[:, 1:].copy()
    criteria = criteria.apply(pd.to_numeric, errors='coerce') 
    
    if criteria.isnull().values.any():
        raise ValueError("From 2nd to end columns must contain numeric values only")

    n_crit = criteria.shape[1]

    try:
        weights_list = [float(w) for w in weights_str.split(',')]
    except ValueError:
        raise ValueError("Weights must be numeric values separated by commas")

    if len(weights_list) != n_crit:
        raise ValueError("Number of weights must match the number of criteria columns")

    impacts_list = [i.strip() for i in impacts_str.split(',')]
    
    if len(impacts_list) != n_crit:
        raise ValueError("Number of impacts must match the number of criteria columns")
    
    if not all(im in ['+', '-'] for im in impacts_list):
        raise ValueError("Impacts must be either '+' or '-' and separated by commas")

    return df, np.array(weights_list), impacts_list

def topsis(inp_file, weights, impacts, out_file):
    try:
        df, weights_arr, impacts_list = validate_inputs(inp_file, weights, impacts)

        criteria_data = df.iloc[:, 1:].values.astype(float)
        column_norms = np.sqrt(np.sum(criteria_data**2, axis=0))
        
        if (column_norms == 0).any():
            raise ValueError("Criteria column contains all zeros, cannot normalize.")
            
        normalized_matrix = criteria_data / column_norms
        weighted_matrix = normalized_matrix * weights_arr

        best = []
        worst = []

        for i in range(len(impacts_list)):
            col = weighted_matrix[:, i]
            if impacts_list[i] == '+':
                best.append(np.max(col))
                worst.append(np.min(col))
            else:
                best.append(np.min(col))
                worst.append(np.max(col))
        
        best = np.array(best)
        worst = np.array(worst)

        dist_best = np.sqrt(np.sum((weighted_matrix - best)**2, axis=1))
        dist_worst = np.sqrt(np.sum((weighted_matrix - worst)**2, axis=1))

        total_dist = dist_best + dist_worst
        topsis_score = np.divide(dist_worst, total_dist, out=np.zeros_like(dist_worst), where=total_dist!=0)

        df['Topsis Score'] = topsis_score
        df['Rank'] = df['Topsis Score'].rank(ascending=False, method='dense').astype(int)

        df.to_csv(out_file, index=False)
        print(f"File saved to {out_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 5:
        print("Error: Wrong number of arguments.")
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)

    inp_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    out_file = sys.argv[4]

    topsis(inp_file, weights, impacts, out_file)

if __name__ == "__main__":
    main()