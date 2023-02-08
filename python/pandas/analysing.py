import pandas as pd

# Count a group size and add it to the original dataframe
df['group_counts'] = df.groupby(by=['col_one', 'col_two'])['id_col'].transform('count')
