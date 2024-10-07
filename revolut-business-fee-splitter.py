import pandas as pd
import tkinter as tk
from tkinter import filedialog

DEBUG = False

# Function to open a file dialog and return the selected file path
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

# Load the original CSV file
# input_file_path = '2023-revolut-business-EUR-monthly-statement_01-Jan-2023_31-Dec-2023.csv'  # Change this to your input CSV file path

# Call the function to get the file path
input_file_path = select_file()

df = pd.read_csv(input_file_path)

# List to hold processed rows
processed_rows = []
data_row = {}
fee_row = {}

# Iterate through the DataFrame rows
for index, row in df.iterrows():
    # Create the row dictionary
    data_row = {
        "Date completed (UTC)": row["Date completed (UTC)"],
        "Description": row["Description"],
        "Row Amount": row["Amount"],
        "Transaction Type": row['Type'],
        "Original Currency": row['Orig currency'],
        "Original Amount": row['Orig amount'],
        "Payment Currency": row['Payment currency'],
        "Row Amount": row['Amount'],
        "Total Amount": row['Total amount'],
        "Exchange Rate": row['Exchange rate'],
        "Fee": row['Fee'],
        "Fee Currency": row['Fee currency']	,
        "Balance": row['Balance'],
        "MCC (Merchant Category Code)": row["MCC"]
    }

    processed_rows.append(data_row)

    if row['Fee'] != 0:
        fee_row = {
            "Date completed (UTC)": row["Date completed (UTC)"],
            "Description": row["Description"],
            "Row Amount": row["Fee"],
            "Transaction Type": row['Type'],
            "Fee Currency": row['Fee currency']
        }
        processed_rows.append(fee_row)
    else:
        fee_row = {}
    if DEBUG == True:
        print(f"Entry row is: {data_row}")
        print(f"Fee row is: {fee_row}")
        input("Press Enter to continue...")


# Create a new DataFrame from the processed rows
processed_df = pd.DataFrame(processed_rows)

# Save to CSV with the original name plus '_processed_for_freeagent'
original_name = input_file_path  # Replace with your actual filename
saved_file_name = original_name.replace('.csv', '_freeagent_formatted.csv')
processed_df.to_csv(saved_file_name, index=False)

print("Processed data saved successfully.")
print("\nNow creating another version of the processed file so that it can be uploaded to FreeAgent.")

# Call the function to get the file path
# input_file_path = select_file()
input_file_path = saved_file_name

df = pd.read_csv(input_file_path)

# Select the first 3 rows and the specified columns
columns_to_select = [
    "Date completed (UTC)",
    "Description",
    "Row Amount"
]

# Create a new DataFrame with only the first 3 rows and the selected columns
processed_df = df[columns_to_select]

# # Rename the columns as needed
# processed_df.columns = [
#     "Date completed (UTC)",
#     "Description",
#     "Row Amount"
# ]

# Format the 'Date completed (UTC)' column to dd/mm/yyyy
processed_df["Date completed (UTC)"] = pd.to_datetime(processed_df["Date completed (UTC)"]).dt.strftime('%d/%m/%Y')

# Format the 'Row Amount' column to 2 decimal places while maintaining sign
processed_df["Row Amount"] = processed_df["Row Amount"].astype(float).apply(lambda x: f"{x:,.2f}")

# Save to a new CSV file
processed_df.to_csv(saved_file_name.replace('.csv', '_processed.csv'), index=False)

print("Processed data saved successfully.")