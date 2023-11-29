import smtplib
from email.message import EmailMessage
from typing import List


def send_email(
    subject: str, body: str, to_emails: List[str], from_email: str, password: str
) -> None:
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
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
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
        "your-password",
    )
