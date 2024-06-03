# import pandas as pd

# def drop_column(input_file, output_file, column_to_drop):
#     # Step 1: Read the CSV file
#     df = pd.read_csv(input_file)

#     # Step 2: Drop the specified column
#     if column_to_drop in df.columns:
#         df.drop(column_to_drop, axis=1, inplace=True)
#         print(f"Column '{column_to_drop}' dropped successfully.")
#     else:
#         print(f"Column '{column_to_drop}' not found in the CSV file.")

#     # Step 3: Save the modified DataFrame to a new CSV file
#     df.to_csv(output_file, index=False)
#     print(f"Data saved to '{output_file}'.")

# if __name__ == "__main__":
#     input_file_path = "D:\judicial anaysis\csv\Saare codes\imp files\cases_2010_with_names(all)(main file).csv"   # Replace with the path to your input CSV file
#     output_file_path = "output_file(droped column).csv" # Replace with the desired output CSV file path
#     column_to_drop = "appended_district_name"      # Replace with the name of the column to be dropped

#     drop_column(input_file_path, output_file_path, column_to_drop)

import pandas as pd
from tqdm import tqdm

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

if __name__ == "__main__":
    main_file_path = "D:\judicial anaysis\csv\Saare codes\output_file(droped column).csv"  # Replace with the path to your main CSV file
    keys_file_path = "D:\judicial anaysis\csv\keys\keys\cases_district_key.csv"  # Replace with the path to your keys CSV file

    append_district_names(main_file_path, keys_file_path)
