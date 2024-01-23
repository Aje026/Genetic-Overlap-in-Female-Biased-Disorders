import pandas as pd
import numpy as np
from itertools import combinations


# Load file to dataframe
df = pd.read_csv('snps_all.txt', sep='\t', index_col=0)

# Set a seed for reproducibility
np.random.seed(42)

num_iterations = 10

# Get all possible combinations of disorders
all_combinations = []
for r in range(2,len(df)+1):
    all_combinations.extend(list(combinations(df.columns, r)))

# Create an empty DataFrame with rows as each combination and columns for storing counts in each iteration
counts_df = pd.DataFrame(index=all_combinations, columns=range(1,num_iterations+1))

# Perform the iterations
for i in range(1,num_iterations+1):
    # Permute the columns independently
    permuted_df = df.apply(np.random.permutation, axis=0)

    iteration_counts = []

    # Count occurrences for each combination in this iteration
    for combo in all_combinations:
        # Check if all disorders in the combination are present in each row
        count = (permuted_df[list(combo)] == 1).all(axis=1).sum()
        iteration_counts.append(count)

    # Store the counts for this iteration in the dataFrame
    counts_df[i] = iteration_counts

# Write dataframe to file
counts_df.to_csv('unique_all_snps_from_binary.txt', sep='\t')