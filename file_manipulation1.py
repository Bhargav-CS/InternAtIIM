import pandas as pd
from tqdm import tqdm

cases_2010_file = "cases_2010_with_names.csv"
cases_state_key_file = 'D:\judicial anaysis\csv\keys\keys\cases_state_key.csv'

# Read the 'cases_2010.csv' file
df_cases_2010 = pd.read_csv(cases_2010_file)

# Read the 'cases_state_key.csv' file
df_cases_state_key = pd.read_csv(cases_state_key_file)

# Create a new column 'appended_state_name' in the 'df_cases_2010' dataframe
df_cases_2010['appended_state_name'] = ""

# Update the 'appended_state_name' column based on 'state_code' key
with tqdm(total=len(df_cases_2010), ncols=80, desc="Progress") as pbar:
    for index, row in df_cases_2010.iterrows():
        state_code = row['state_code']
        state_name = df_cases_state_key.loc[df_cases_state_key['state_code'] == state_code, 'state_name'].values
        if len(state_name) > 0:
            df_cases_2010.at[index, 'appended_state_name'] = state_name[0]
        pbar.update(1)

# Save the updated data to a new CSV file
output_file_path = 'cases_2010_with_appendedentries.csv'
df_cases_2010.to_csv(output_file_path, index=False)
