
from random import seed
import os
import pandas as pd
from itertools import combinations
import scipy.cluster.hierarchy as sch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import hypergeom
from sklearn.preprocessing import StandardScaler
from collections import Counter
from scipy.cluster import hierarchy
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import pdist, squareform

#set seed for reproducibility
np.random.seed(42)

def read_SNPs_and_genes(path, column_names):
 
    df_list = []
    disorder_names = []

    # Iterate through files in the directory
    for filename in os.listdir(path):
        if filename.endswith('.txt'):  # Process only .txt files
            # Extract disorder name from the filename
            disorder_name = filename.split('_')[1].split('.')[0]
            disorder_names.append(disorder_name)

            # Read the file as a DataFrame
            file_path = os.path.join(path, filename)
            df = pd.read_csv(file_path, sep='\t', low_memory=False)

            # Choose columns of interest
            df['disorder'] = disorder_name
            df = df[column_names]
            df = df.dropna()
            df.reset_index(inplace=True, drop=True)
            # Append the DataFrame to the list
            df_list.append(df)
    return df_list

snp_df_list = read_SNPs_and_genes('FUMA_dowloads_all_tissue/SNPs',['uniqID','rsID','gwasP','disorder'])
gene_df_list = read_SNPs_and_genes('FUMA_dowloads_all_tissue/eQTL',['uniqID','symbol','tissue','disorder'])

""" print(len(snp_df_list), len(gene_df_list))
print(snp_df_list[0].head())
print(gene_df_list[0].head()) """

def make_binary_matrix(df_list, column1,column2):
    concatenated= pd.concat(df_list)
    df = concatenated[[column1, column2]]
    
    return df.pivot_table(index=column1, columns=column2, aggfunc=lambda x: 1, fill_value=0)


all_snps_binary = make_binary_matrix(snp_df_list, 'rsID', 'disorder')
all_genes_binary = make_binary_matrix(gene_df_list,'symbol', 'disorder')

print(all_snps_binary.sum(axis=0))
print(all_genes_binary.sum(axis=0))



def find_max_row(binary_df):
    row_sums = binary_df.sum(axis=1)

    # Find the maximum sum
    max_row_sum = row_sums.max()
    return max_row_sum


max_combo_snps = find_max_row(all_snps_binary)
max_combo_genes = find_max_row(all_genes_binary)

print('max snps: ', max_combo_snps)
print('max genes: ', max_combo_genes)



def count_combos(binary_df, max_combo, randomized=False):
    
    # Get all possible combinations of disorders
    all_combinations = []
    for r in range(2, max_combo):
        all_combinations.extend(list(combinations(binary_df.columns, r)))
        print('all combos found')
    # Create an empty DataFrame to store counts
    counts_df = pd.DataFrame(index=all_combinations)

    if randomized:
          # Set a seed for reproducibility in randomized data
        num_iterations = 10
        # Perform the iterations for randomized data
        for i in range(1, num_iterations+1):
            # Permute the columns independently
            permuted_df = binary_df.apply(np.random.permutation, axis=0)
            print('permuted')
            # Count occurrences for each combination in this iteration
            iteration_counts = [(permuted_df[list(combo)] == 1).all(axis=1).sum() for combo in all_combinations]
            print('permuted and counted')
            # Store the counts for this iteration in the DataFrame
            counts_df[i] = iteration_counts
    else:
        # Count occurrences for each combination in the real data
        iteration_counts = [(binary_df[list(combo)] == 1).all(axis=1).sum() for combo in all_combinations]
        print('counted not permuted')
        # Store the counts in the DataFrame
        counts_df['Count'] = iteration_counts

    return counts_df

snp_combos = count_combos(all_snps_binary, 6)
snp_combos_rand = count_combos(all_snps_binary, 6, randomized=True)
gene_combos = count_combos(all_genes_binary, 6)
gene_combos_rand = count_combos(all_genes_binary, 6, randomized=True)



def calculate_z_score(df, df_rand, threshold, count):
    
    #calculate mean and standard deviation
    means = round(df_rand.mean(axis=1),2)
    std = round(df_rand.std(axis=1),2)

    df_rand['mean'] = means
    df_rand['std'] = std
    df_rand['actual'] = df['Count']
    
    new_df = df_rand[['actual', 'mean', 'std']]
    
    #Make copies to avoid warnings
    new_df_copy = new_df.copy()
    
    # Calculate Z-scores 
    new_df_copy['z-score'] = round((new_df_copy['actual'] - new_df_copy['mean']) / new_df_copy['std'],2)
    
    sorted_df = new_df_copy.sort_values(by='z-score', ascending=False)
    
    # Replace infinite values in the "z-score" column with NaN
    sorted_df['z-score'].replace([np.inf, -np.inf], np.nan, inplace=True)
    
    # Drop rows with NaN values in the "z-score" column
    sorted_df.dropna(subset=['z-score'], how='any', inplace=True)

    return sorted_df[(sorted_df['z-score'] >= threshold) & (sorted_df['actual'] >= count)]    


z2_snps = calculate_z_score(snp_combos, snp_combos_rand, 2, 5)
z3_snps = calculate_z_score(snp_combos, snp_combos_rand, 3, 5)
z2_genes = calculate_z_score(gene_combos, gene_combos_rand, 2, 5)
z3_genes = calculate_z_score(gene_combos, gene_combos_rand, 3, 5)

print('Number of combinations sharing SNPs with z-value >= 2: ', len(z2_snps))
print('Number of combinations sharing SNPs with z-value >= 3: ', len(z3_snps))
print('Number of combinations sharing genes with z-value >= 2: ', len(z2_genes))
print('Number of combinations sharing genes with z-value >= 3: ', len(z3_genes))

z2_snps.to_csv('snps_zscore2.csv')
z3_snps.to_csv('snps_zscore3.csv')
z2_genes.to_csv('genes_zscore2.csv')
z3_genes.to_csv('genes_zscore3.csv')

