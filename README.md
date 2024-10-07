# revolut-business-to-freeagent
A utility script that converts Revolut Business CSV statements into FreeAgent-compatible format, simplifying the import process for accounting data.

## Features
- Converts Revolut Business CSV into a FreeAgent-compatible format.
- Automatically handles transaction fees by creating separate fee entries.
- Formats dates and amounts for smooth import into FreeAgent.

## How It Works
1. The script loads your Revolut Business CSV statement.
2. Processes the CSV to match FreeAgent's required format:
   - Handles fees separately from transaction amounts.
   - Reformats date and amount fields.
3. Saves the processed data as a new CSV file, ready for import into FreeAgent.

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/revolut-business-to-freeagent.git
    ```

2. Install the required dependencies:
    ```bash
    pip install pandas
    ```

3. Run the script:
    ```bash
    python script_name.py
    ```

4. A file dialog will open, allowing you to select your Revolut Business CSV statement.

5. The script will process the file and save the results as `<your-file-name>_freeagent_formatted.csv` and `<your-file-name>_processed.csv`.

## FreeAgent CSV Format
For more details on the structure required by FreeAgent, refer to their official guide on formatting CSV files for bank statement uploads:  
[How to format a CSV file to upload a bank statement](https://support.freeagent.com/hc/en-gb/articles/115001222564-How-to-format-a-CSV-file-to-upload-a-bank-statement).

**Please Note:** The information in this document has been tested as of 30 September 2024. Changes made by FreeAgent to their input format may disrupt the program, so it is advisable to check the linked guide for the latest requirements regarding your type of statement.

## Requirements
- Python 3.x
- pandas
- tkinter (for file selection dialog)

## Example

- Input: `2023-revolut-business-EUR-monthly-statement.csv`
- Output: 
  - `2023-revolut-business-EUR-monthly-statement_freeagent_formatted.csv`
  - `2023-revolut-business-EUR-monthly-statement_processed.csv`

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.
