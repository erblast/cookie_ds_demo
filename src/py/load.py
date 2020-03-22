

import seaborn as sns
import pandas as pd

with open(snakemake.config["config_file"]["exec"], 'r') as f:
    params = yaml.safe_load(f)

df = sns.load_dataset(params['dataset'])

df.to_feather(snakemake.output[0])

print('load finished')
