# snippet
Snippets to speed up development of Python projects.
1. google_sheets: connect and manipulate a Google Sheets document

## google_sheets
- read_sheet(): displays sheet in 2D array of data
- update_sheet(): updates a specific cell with new data
- authenticate_gsheets(): returns authenticated client
##### configure
- create service account, download creds into credentials.json
- give service account permissions to google sheet
- set sheet_id and sheet_name
- send it