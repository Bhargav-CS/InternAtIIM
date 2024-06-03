import csv

# Specify the input and output file paths
input_file = r'E:\ecourts\keys\purpose_name_key.csv'
output_file = '2010-purpose-key.csv'

# Specify the target year
target_year = '2010'

# Read the input CSV file
with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader if row['year'] == target_year]

# Write the filtered rows to a new CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Filtered entries for year {target_year} have been written to {output_file}.")
