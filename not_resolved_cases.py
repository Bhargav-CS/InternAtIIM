import pandas as pd
from tqdm import tqdm

# Replace 'input_file.csv' with the path to your CSV file
input_file = 'D:\judicial anaysis\csv\Saare codes\imp files\output_file.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Convert the 'date_of_decision' column to datetime format
df['date_of_decision'] = pd.to_datetime(df['date_of_decision'], errors='coerce')

# Filter rows where 'date_of_decision' is in the year 2010
filtered_df = df[df['date_of_decision'].dt.year == 2010]

# Define the output file path
output_file = 'filtered_data.csv'

# Get the total number of rows to use in the tqdm progress bar
total_rows = len(filtered_df)

# Save the filtered DataFrame to a new CSV file with a progress bar
with tqdm(total=total_rows, desc="Saving filtered data") as pbar:
    filtered_df.to_csv(output_file, index=False, chunksize=1000)  # You can adjust the chunksize if needed
    pbar.update(total_rows)

print("Filtered data has been saved to 'filtered_data(1).csv'.")
