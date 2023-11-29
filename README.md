# snippet
Snippets to speed up development of Python projects.
1. google_sheets: connect and manipulate a Google Sheets document
2. discord_bot: listens for command, also runs scheduled background command
3. send_mail: using Google/SMTP, send an email message from gmail account
4. sendgrid_mail: send an email message using sendgrid account
5. twilio_sms: send sms text message with twilio account

## google_sheets
- read_sheet(): displays sheet in 2D array of data
- update_sheet(): updates a specific cell with new data
- authenticate_gsheets(): returns authenticated client
##### configure
- create service account, download creds into credentials.json
- give service account permissions to google sheet
- set sheet_id and sheet_name

## discord_bot
- responds to !hello
- runs command every minute
##### configure
- requires bot to be setup
- need to insert bot token
- need to edit channel ID, if used in task

## send_mail
- send an email using your gmail account
- needs some configuration
##### configure
- sign into Google, ensure 2FA is enabled
- create an app password
- replace username and email in the script
- make sure you test your email before using in production

## sendgrid_mail
- send an email using sendmail
- add api key before sending

## twilio_sms
- fill in sid and auth token
- setup twilio phone number
- setup recipient and body of text