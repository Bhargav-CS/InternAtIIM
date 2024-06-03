import pandas as pd
from tqdm import tqdm

def merge_csv_files(file1, file2, output_file):
    # Step 1: Read the two CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Step 2: Merge the two DataFrames based on 'district name' column (outer join to handle missing values)
    merged_df = pd.merge(df1, df2, on='district', how='outer')

    # Step 3: Handle missing values (replace NaN with 0 in the 'resolved cases' column)
    merged_df['resolved'] = merged_df['resolved'].fillna(0).astype(int)

    # Step 4: Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"Merged data saved to '{output_file}'.")

if __name__ == "__main__":
    file1_path = "D:\judicial anaysis\csv\Saare codes\imp files\district_counts.csv"   # Replace with the path to your first CSV file
    file2_path = "D:\judicial anaysis\csv\Saare codes\imp files\district_counts(resolved).csv"   # Replace with the path to your second CSV file
    output_file_path = "file3.csv"  # Replace with the desired output CSV file path

    merge_csv_files(file1_path, file2_path, output_file_path)
