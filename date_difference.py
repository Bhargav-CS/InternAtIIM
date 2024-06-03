import csv
from datetime import datetime, timedelta
from tqdm import tqdm

def calculate_date_difference(date1, date2, date_format):
    # Convert string dates to datetime objects
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)

    # Calculate the difference between the dates
    difference = abs((datetime2 - datetime1).days)

    return difference

# Path to the CSV file
csv_file = r"D:\judicial anaysis\csv\Saare codes\cases_2010_with_stateanddistrictanddispandcourt_name.csv"

# Path to save the updated CSV file
output_csv_file = "dates_with_difference.csv"

# Specify the column names for the dates and date format
date_column1 = "date_of_filing"  # Modify this to the actual column name
date_column2 = "date_of_decision"  # Modify this to the actual column name
date_format = "%Y-%m-%d"  # Modify this to the actual date format in the CSV

# Get the total number of rows in the CSV file
with open(csv_file, "r") as file:
    num_rows = sum(1 for line in file) - 1  # Exclude the header row

# Open the CSV file for reading
with open(csv_file, "r") as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Read the header row
    header = reader.fieldnames

    # Append a new column header
    header.append("Difference (Days)")

    # Read the remaining rows and calculate the date difference
    rows = []
    for row in tqdm(reader, total=num_rows, desc="Calculating Difference"):
        date1 = row[date_column1]
        date2 = row[date_column2]
        
        try:
            difference = calculate_date_difference(date1, date2, date_format)
        except ValueError:
            difference = "Invalid Date"
            
        row["Difference (Days)"] = str(difference)
        rows.append(row)

# Open the output CSV file for writing
with open(output_csv_file, "w", newline="") as file:
    # Create a CSV writer object
    writer = csv.DictWriter(file, fieldnames=header)

    # Write the header row
    writer.writeheader()

    # Write the updated rows
    writer.writerows(rows)

print("Date difference calculation complete.")
