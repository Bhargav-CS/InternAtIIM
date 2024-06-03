import pandas as pd
from tqdm import tqdm

def column_appender(input_file, state_key_file, district_key_file, output_file):
    df_cases_2010 = pd.read_csv(input_file)
    df_cases_state_key = pd.read_csv(state_key_file)
    df_cases_district_key = pd.read_csv(district_key_file)

    # Create a dictionary mapping (state_code, dist_code) to district names
    district_mapping = {}
    for _, row in df_cases_district_key.iterrows():
        district_mapping[(row['state_code'], row['dist_code'])] = row['district_name']

    df_cases_2010['appended_state_name'] = ""
    df_cases_2010['appended_district_name'] = ""

    with tqdm(total=len(df_cases_2010), ncols=80, desc="Progress Column Appender") as pbar:
        for index, row in df_cases_2010.iterrows():
            state_code = row['state_code']
            dist_code = row['dist_code']

            state_name = df_cases_state_key.loc[df_cases_state_key['state_code'] == state_code, 'state_name'].values
            if len(state_name) > 0:
                df_cases_2010.at[index, 'appended_state_name'] = state_name[0]

            # Find the corresponding district name based on the state_code and dist_code
            district_name = district_mapping.get((state_code, dist_code))
            if district_name is None:
                # If district name not found for the given state_code and dist_code, add a placeholder or 'N/A'
                district_name = 'N/A'
            df_cases_2010.at[index, 'appended_district_name'] = district_name

            pbar.update(1)

    df_cases_2010.to_csv(output_file, index=False)
    print(f"Data with appended state and district names saved to '{output_file}'.")

def extract_rows_by_district(input_file, output_file, column_name):
    df = pd.read_csv(input_file)
    unique_districts_counts = df['appended_district_name'].value_counts().reset_index()
    unique_districts_counts.columns = ['district', column_name]  # Use the provided column_name for count

    print(f"Unique Districts with {column_name}:")
    print(unique_districts_counts)

    tqdm_total = len(unique_districts_counts)
    with tqdm(total=tqdm_total, ncols=80, desc="Saving district counts") as pbar:
        with open(output_file, 'w') as f:
            f.write("district," + column_name + "\n")
            for _, row in unique_districts_counts.iterrows():
                district_name = row['district']
                count_value = row[column_name]
                f.write(f"{district_name},{count_value}\n")
                pbar.update(1)

    print(f"Data with {column_name} saved to '{output_file}'.")

def merge_csv_files(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged_df = pd.merge(df1, df2, on='district', how='outer')
    merged_df['resolved'] = merged_df['resolved'].fillna(0).astype(int)

    with tqdm(total=len(merged_df), ncols=80, desc="Merging CSV files") as pbar:
        merged_df.to_csv(output_file, index=False)
        pbar.update(len(merged_df))

    print(f"Merged data saved to '{output_file}'.")

def calculate_disposal_rate(input_file, output_file):
    df = pd.read_csv(input_file)

    # Handle potential division by zero and missing values
    df['disposal_rate'] = df['resolved'] / df['total_cases'].replace(0, pd.NA)

    with tqdm(total=len(df), ncols=80, desc="Calculating Disposal Rate") as pbar:
        df.to_csv(output_file, index=False)
        pbar.update(len(df))

    print(f"Data with disposal rate saved to '{output_file}'.")

if __name__ == "__main__":
    cases_2011_file = "D:\judicial anaysis\csv\Saare codes\Random_entries_2010.csv"
    cases_state_key_file = "D:\judicial anaysis\csv\keys\keys\cases_state_key.csv"
    keys_file_path = "D:\judicial anaysis\csv\keys\keys\cases_district_key.csv"

    # Step 1: Run columnappender.py
    column_appender(cases_2011_file, cases_state_key_file, keys_file_path, "output_file2011.csv")

    # Step 2: Run something.py for total cases
    extract_rows_by_district("output_file2011.csv", "district_counts2011.csv", "total_cases")

    # Step 3: Run not_resolved_cases.py
    df = pd.read_csv("output_file2011.csv")
    df['date_of_decision'] = pd.to_datetime(df['date_of_decision'], errors='coerce')  # Convert to datetime format
    filtered_df = df[df['date_of_decision'].dt.year == 2010]
    filtered_df.to_csv("filtered_data2011.csv", index=False)
    print("Filtered data has been saved to 'filtered_data2011.csv'.")

    # Step 4: Run something.py again for resolved cases
    extract_rows_by_district("filtered_data2011.csv", "district_counts(resolved)2011.csv", "resolved")

    # Step 5: Run putbullas0.py to merge total cases and resolved cases
    merge_csv_files("district_counts2011.csv", "district_counts(resolved)2011.csv", "file3_2011.csv")

    # Step 6: Run disposa_rate_Calc.py to calculate disposal rate
    calculate_disposal_rate("file3_2011.csv", "disposal-rate_file2011.csv")
