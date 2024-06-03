import pandas as pd
from tqdm import tqdm

cases_2010_file = "D:\judicial anaysis\csv\cases\cases\cases_2011.csv"
cases_state_key_file = "D:\judicial anaysis\csv\keys\keys\cases_state_key.csv"
keys_file_path = "D:\judicial anaysis\csv\keys\keys\cases_district_key.csv"
# cases_purpose_key_file = "D:\judicial anaysis\csv\Saare codes\M2010-purpose-key.csv"
# cases_type_key_file = "D:\judicial anaysis\csv\Saare codes\M2010-type-name.csv"



# Read the 'cases_2010.csv' file
df_cases_2010 = pd.read_csv(cases_2010_file)

# Read the 'cases_state_key.csv' file
df_cases_state_key = pd.read_csv(cases_state_key_file)

# Create new columns 'appended_state_name'
df_cases_2010['appended_state_name'] = ""


# Update the 'appended_state_name' column based on 'state_code' key
with tqdm(total=len(df_cases_2010), ncols=80, desc="Progress") as pbar:
    for index, row in df_cases_2010.iterrows():
        state_code = row['state_code']
        state_name = df_cases_state_key.loc[df_cases_state_key['state_code'] == state_code, 'state_name'].values
        if len(state_name) > 0:
            df_cases_2010.at[index, 'appended_state_name'] = state_name[0]
        pbar.update(1)


def append_district_names(main_file, keys_file):
    # Step 1: Read the main and keys CSV files
    main_df = pd.read_csv(main_file)
    keys_df = pd.read_csv(keys_file)

    # Step 2: Create a dictionary mapping (state_code, dist_code) to district names
    district_mapping = {}
    for _, row in keys_df.iterrows():
        district_mapping[(row['state_code'], row['dist_code'])] = row['district_name']

    # Step 3: Iterate through the main DataFrame and append district names based on keys
    appended_district_names = []
    tqdm_total = len(main_df)

    print("Appending district names:")
    for _, row in tqdm(main_df.iterrows(), total=tqdm_total):
        state_code = row['state_code']
        dist_code = row['dist_code']

        # Find the corresponding district name based on the state_code and dist_code
        district_name = district_mapping.get((state_code, dist_code))

        if district_name is None:
            # If district name not found for the given state_code and dist_code, add a placeholder or 'N/A'
            district_name = 'N/A'

        appended_district_names.append(district_name)

    # Step 4: Append the new 'appended_district_name' column to the main DataFrame
    main_df['appended_district_name'] = appended_district_names

    # Step 5: Save the modified DataFrame to a new CSV file
    output_file = "output_file.csv"  # Replace with the desired output CSV file path
    main_df.to_csv(output_file, index=False)
    print(f"Data with appended district names saved to '{output_file}'.")


# Save the updated data to a new CSV file
output_file_path = 'cases_2011_with_StatesandDistricts.csv'
df_cases_2010.to_csv(output_file_path, index=False)
append_district_names(output_file_path, keys_file_path)

