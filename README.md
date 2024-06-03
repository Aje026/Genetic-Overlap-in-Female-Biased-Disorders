# Genetic overlap in female-biased disorders and diseases

## This project aimed to find overlaps between disorders that mainly affects women.
Overlap between cases of disorders and diseases and genetic overlap has been investigated



Description of the files in this repository:

- get.rsID.py adds rsID to the files that misses this. 

- analysis.ipynb contains the whole pipeline using SNP and eQTL files from FUMA analysis.

- ldscore.sh is a Shell script to automate the LDSC analysis for all the disorders and diseases
  
- extract_table.py extracts the relevant information in the log files produced by LDSC software and produces files to be used in correlation.ipynb
  
- correlation.ipynb produces plots to visualize the correlations from LDSC. It reads in the files that are produced by extract_table.py

- z_score_SNPs.csv and z_score_genes.csv are files with all combinarions of disorders and diseases with z-value above 3, produced by analysis.ipynb
  
