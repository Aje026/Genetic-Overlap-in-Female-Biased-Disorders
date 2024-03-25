import pandas as pd

preec = pd.read_csv('preeclampsia_new.tsv', sep=' ')
preec = preec.drop(columns=['Unnamed: 11'])
preec = preec[preec['P-value'] <= 0.05]
preec.to_csv('preeclampsia_filtered.tsv', sep='\t', index=False)

print(preec.head())

gh = pd.read_csv('gh_new.tsv', sep=' ')
gh = gh.drop(columns=['Unnamed: 11'])
gh = gh[gh['P-value'] <= 0.05]
gh.to_csv('gh_filtered.tsv', sep='\t', index=False)

print(gh.head())