import pandas as pd

panic = pd.read_csv('pgc-panic2019.vcf.tsv', sep='\t', skiprows=72)

#hoarding.head()

panic.to_csv('panic.txt', sep='\t', index=False)