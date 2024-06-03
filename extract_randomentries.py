# extract random entries 

import pandas as pd
import random
from tqdm import tqdm

def extract_random_entries(input_file, output_file, num_entries):
    # Count the total number of entries in the CSV file
    total_entries = sum(1 for line in open(input_file)) - 1  # Subtract 1 to exclude the header row

    # Generate a random sample of line numbers
    random_indices = random.sample(range(1, total_entries + 1), num_entries)

    # Read the CSV file and extract the random entries
    df = pd.DataFrame()
    with tqdm(total=num_entries, ncols=80, desc="Progress") as pbar:
        for i, chunk in enumerate(pd.read_csv(input_file, chunksize=1000)):
            chunk['row_index'] = i * 1000 + chunk.index + 1
            chunk = chunk[chunk['row_index'].isin(random_indices)]
            df = pd.concat([df, chunk])
            pbar.update(chunk.shape[0])
            if df.shape[0] >= num_entries:
                break
    df.drop('row_index', axis=1, inplace=True)  # Remove the temporary 'row_index' column

    # Write the extracted data to a new CSV file
    df.to_csv(output_file, index=False)

# Example usage:
input_file = 'D:\\judicial anaysis\\csv\\acts_sections\\acts_sections.csv'
output_file = 'Random_entries_2010(acts_section).csv'
num_entries = 100000

extract_random_entries(input_file, output_file, num_entries)
