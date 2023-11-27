import gspread
import warnings
from typing import List
from oauth2client.service_account import ServiceAccountCredentials


# Temporarily suppress deprecation warning
warnings.filterwarnings("ignore", category=DeprecationWarning)


def authenticate_gsheets(json_keyfile: str) -> gspread.Client:
    """
    Authenticates Google Sheets using OAuth2 credentials.

    Args:
    json_keyfile (str): The path to the JSON key file for Google Service Account.

    Returns:
    gspread.Client: Authenticated gspread client.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)

    client = gspread.authorize(creds)
    return client


def read_sheet(
    client: gspread.Client, sheet_id: str, sheet_name: str
) -> List[List[str]]:
    """
    Reads data from a specific Google Sheet.

    Args:
    client (gspread.Client): Authenticated gspread client.
    sheet_id (str): The ID of the Google Sheet.
    sheet_name (str): The name of the specific sheet to read.

    Returns:
    List[List[str]]: 2D list containing the data from the sheet.
    """
    sheet = client.open_by_key(sheet_id).worksheet(sheet_name)
    return sheet.get_all_values()


def update_sheet(
    client: gspread.Client,
    sheet_id: str,
    sheet_name: str,
    row: int,
    col: int,
    value: str,
):
    """
    Updates a specific cell in a Google Sheet.

    Args:
    client (gspread.Client): Authenticated gspread client.
    sheet_id (str): The ID of the Google Sheet.
    sheet_name (str): The name of the specific sheet to update.
    row (int): Row number of the cell to update.
    col (int): Column number of the cell to update.
    value (str): The new value to set in the cell.
    """
    sheet = client.open_by_key(sheet_id).worksheet(sheet_name)
    sheet.update_cell(row, col, value)


# Example usage
json_keyfile = "credentials.json"  # Replace with your JSON key file path
sheet_id = (
    "0123456789abcdef"  # Replace with your Google Sheet ID
)
sheet_name = "Sheet1"  # Replace with your specific sheet name

client = authenticate_gsheets(json_keyfile)

# Reading data from the sheet
data = read_sheet(client, sheet_id, sheet_name)
print("Sheet data:", data)

# Updating a cell in the sheet
update_sheet(client, sheet_id, sheet_name, row=20, col=1, value="New Value")
