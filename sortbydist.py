import pandas as pd
from tqdm import tqdm

def extract_rows_by_district(input_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Step 2: Read the appended_district_name column and get unique values
    unique_districts = df['appended_district_name'].unique()

    # Step 3: Print unique values
    print("Unique Districts:")
    for district in tqdm(unique_districts):
        print(district)

    # Step 4 and 5: Extract rows for each unique district and create separate files
    for district in tqdm(unique_districts, desc="Processing districts", unit="district"):
        district_df = df[df['appended_district_name'] == district]
        output_filename = f"{district}.csv"
        district_df.to_csv(output_filename, index=False)
        tqdm.write(f"Created file: {output_filename}")

if __name__ == "__main__":
    input_file_path = "output_file.csv"  # Replace with the path to your CSV file
    extract_rows_by_district(input_file_path)