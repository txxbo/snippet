import smtplib
from email.message import EmailMessage
from typing import List

def send_email(subject: str, body: str, to_emails: List[str], from_email: str, password: str) -> None:
    """
    Send an email using the SMTP protocol.

    Args:
    subject (str): The subject of the email.
    body (str): The body of the email.
    to_emails (List[str]): A list of recipient email addresses.
    from_email (str): The sender's email address.
    password (str): The password or app-specific password for the sender's email account.

    Example:
    send_email(
        "Test Subject", 
        "This is a test email", 
        ["recipient@example.com"], 
        "your-email@gmail.com", 
        "your-password"
    )
    """
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)  # Login to the SMTP server
        smtp.send_message(msg)  # Send the email

    print("Email sent successfully.")

# Example usage
if __name__ == "__main__":
    send_email(
        "Test Subject",
        "This is a test email",
        ["recipient@example.com"],
        "your-email@gmail.com",
        "your-password"
    )

"""

Generate an App Password:

Go to your Google Account settings. You can navigate there by clicking on your profile picture in Gmail and selecting “Manage your Google Account.”

On the left side, click on “Security.”

Under the “Signing in to Google” section, look for “2-Step Verification” and make sure it is turned on. If not, follow the steps to enable it.

Scroll down to the “App passwords” section and click on it.

You may be asked to sign in again. After signing in, under “Select app,” choose “Mail.”

Under “Select device,” choose “Other” and type in a custom name, like “Python Script.”

Click on “Generate.” Google will generate a 16-character password. Copy this password.

Use this App Password in Your Script:

In the script where it asks for “your-password,” use the 16-character app password you just generated.

Email and Password in the Script:

Replace “your-email@gmail.com” with your Gmail address.

Replace “your-password” with either your app password (if using 2FA) or your regular Gmail password (if less secure apps are allowed).

Test the Script Safely:

Before using it extensively, test the script with a small number of emails to ensure it works correctly and doesn't trigger any spam filters.

Security Note:

Be cautious with your app password or regular password. Do not share the script with others without removing your credentials.

Consider using environment variables or other secure methods to handle your credentials in the script.

"""