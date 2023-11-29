import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from typing import List


def send_email_via_sendgrid(
    subject: str, body: str, to_emails: List[str], from_email: str, api_key: str
) -> None:
    """
    Send an email using SendGrid.

    Args:
    subject (str): The subject of the email.
    body (str): The body of the email.
    to_emails (List[str]): A list of recipient email addresses.
    from_email (str): The sender's email address.
    api_key (str): The API key for SendGrid.

    Example:
    send_email_via_sendgrid(
        "Test Subject",
        "This is a test email",
        ["recipient@example.com"],
        "your-email@example.com",
        "your-sendgrid-api-key"
    )
    """
    message = Mail(
        from_email=from_email, to_emails=to_emails, subject=subject, html_content=body
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
        print(response.body)
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    send_email_via_sendgrid(
        "Test Subject",
        "<strong>This is a test email</strong>",
        ["recipient@example.com"],
        "your-email@example.com",
        "your-sendgrid-api-key",
    )
