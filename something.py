import pandas as pd
from tqdm import tqdm

def extract_rows_by_district(input_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Step 2: Read the appended_district_name column and get unique values with counts
    unique_districts_counts = df['appended_district_name'].value_counts().reset_index()
    unique_districts_counts.columns = ['district', 'total_cases']

    # Step 3: Print unique values with counts
    print("Unique Districts with Total Cases:")
    print(unique_districts_counts)

    # Step 4: Save the unique district counts to a new CSV file
    output_file = "district_counts(resolved)2011.csv"  # Replace with the desired output CSV file path

    tqdm_total = len(unique_districts_counts)
    print("Saving district counts to CSV:")
    with open(output_file, 'w') as f:
        f.write("district,total_cases\n")
        for _, row in tqdm(unique_districts_counts.iterrows(), total=tqdm_total):
            district_name = row['district']
            total_cases = row['total_cases']
            f.write(f"{district_name},{total_cases}\n")

    print(f"Data with district counts saved to '{output_file}'.")

if __name__ == "__main__":
    input_file_path = "output_file.csv"  # Replace with the path to your CSV file
    extract_rows_by_district(input_file_path)
