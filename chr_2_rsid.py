from easy_entrez import EntrezAPI
import pandas as pd
import numpy as np
import time
entrez_api = EntrezAPI('your-tool-name','your.email@gmail.com')

df = pd.read_csv('spontanious_preterm_birth.tsv', sep='\t')

df = df[['chromosome', 'base_pair_location']]
chunks = np.array_split(df,1000)
rsid_dfs = []
for df in chunks:
    rsID = []
    for i in range(len(df)):
        results = entrez_api.search(
            dict(chromosome=df['chromosome'][i], organism='human', position=df['base_pair_location'][i]),
            database='snp',
            max_results=10
        )
        # rsID.append('rs'+results.data['esearchresult']['idlist'][-1])
        # Check if any results were found
        idlist = results.data['esearchresult']['idlist']
        if idlist:
            rsID.append('rs' + idlist[-1])
        else:
            rsID.append(None)
            
        time.sleep(1)
    print('one done')
    df['rs_id'] = rsID
    rsid_dfs.append(df)

concat_diabetes = pd.concat(rsid_dfs)
concat_diabetes.to_csv('preterm_birth.txt', sep='\t', index=False)