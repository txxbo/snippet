from twilio.rest import Client
from typing import List

def send_sms_via_twilio(body: str, to_numbers: List[str], from_number: str, account_sid: str, auth_token: str) -> None:
    """
    Send an SMS using Twilio.

    Args:
    body (str): The body of the SMS.
    to_numbers (List[str]): A list of recipient phone numbers.
    from_number (str): The Twilio phone number sending the SMS.
    account_sid (str): The Account SID from Twilio.
    auth_token (str): The Auth Token from Twilio.

    Example:
    send_sms_via_twilio(
        "This is a test SMS", 
        ["+1234567890"], 
        "+10987654321", 
        "your-twilio-account-sid",
        "your-twilio-auth-token"
    )
    """
    client = Client(account_sid, auth_token)

    for number in to_numbers:
        message = client.messages.create(
            body=body,
            from_=from_number,
            to=number
        )
        print(f"Sent message to {number}: {message.sid}")

# Example usage
if __name__ == "__main__":
    send_sms_via_twilio(
        "This is a test SMS!",
        ["+1234567890"],  # Replace with the recipient's phone number
        "+10987654321",   # Replace with your Twilio phone number
        "your-twilio-account-sid",
        "your-twilio-auth-token"
    )
