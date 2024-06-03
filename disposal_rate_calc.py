import pandas as pd

def calculate_disposal_rate(input_file, output_file):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_file)

    # Step 2: Calculate the disposal rate
    df['disposal_rate'] = df['resolved'] / df['totalcases']

    # Step 3: Save the DataFrame with disposal rate to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Data with disposal rate saved to '{output_file}'.")

if __name__ == "__main__":
    input_file_path = "D:\\judicial anaysis\\csv\\Saare codes\\file3.csv"   # Replace with the path to your input CSV file
    output_file_path = "disposal-rate_file.csv"  # Replace with the desired output CSV file path

    calculate_disposal_rate(input_file_path, output_file_path)
