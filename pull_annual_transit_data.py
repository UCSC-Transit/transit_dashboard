import gspread
import pandas as pd
import numpy as np

# function to pull data from google sheets 

def pull_sheet_data(sheet_name, worksheet_name, credentials_file):
    """
    Pulls all records from a specified Google Sheet worksheet into a pandas DataFrame.
    """
    try:
        # Authenticate using the service account credentials
        gc = gspread.service_account(filename=credentials_file)
        
        # Open the Google Sheet by its name
        sh = gc.open(sheet_name)
        
        # Select a specific worksheet
        worksheet = sh.worksheet(worksheet_name)
        
        # Fetch all data as a list of dictionaries (assuming first row is headers)
        data = worksheet.get_all_records()
        
        # Convert the data into a pandas DataFrame for easier analysis
        annual_transit_totals_df = pd.DataFrame(data)


        annual_transit_totals_df.columns = annual_transit_totals_df.iloc[1]
        annual_transit_totals_df = annual_transit_totals_df.iloc[2:]

        annual_transit_totals_df = annual_transit_totals_df.set_index('Date')
        annual_transit_totals_df.index.name = None
        annual_transit_totals_df.columns.name = None

        annual_transit_totals_df = annual_transit_totals_df.replace('', np.nan)
        annual_transit_totals_df = annual_transit_totals_df.dropna(axis=1)

        annual_transit_totals_df = annual_transit_totals_df.apply(pd.to_numeric, errors='coerce')
        annual_transit_totals_df = annual_transit_totals_df.astype('Int64')

        annual_transit_totals_df['EG_morning'] = annual_transit_totals_df["L1-1"] + annual_transit_totals_df["L2-1"] + annual_transit_totals_df["L3-1"]
        annual_transit_totals_df['BT_morning'] = annual_transit_totals_df["L4-1"] + annual_transit_totals_df["L5-1"] + annual_transit_totals_df["L6-1"]
        annual_transit_totals_df['EG_afternoon'] = annual_transit_totals_df["L1-2"] + annual_transit_totals_df["L2-2"] + annual_transit_totals_df["L3-2"]
        annual_transit_totals_df['BT_afternoon'] = annual_transit_totals_df["L4-2"] + annual_transit_totals_df["L5-2"] + annual_transit_totals_df["L6-2"]
        annual_transit_totals_df['EG_Total'] = annual_transit_totals_df["EG_morning"] + annual_transit_totals_df["EG_afternoon"] + annual_transit_totals_df["EG Loop Supplementals"]
        annual_transit_totals_df['BT_Total'] = annual_transit_totals_df["BT_morning"] + annual_transit_totals_df["BT_afternoon"] + annual_transit_totals_df["WG Loop Supplementals"]
        
        return annual_transit_totals_df

    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Error: Spreadsheet named '{sheet_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

