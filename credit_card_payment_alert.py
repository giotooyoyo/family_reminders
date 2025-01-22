import datetime
import json

file_path = "personal_data.json"
with open(file_path, 'r') as file:
    data = json.load(file)
CREDIT_CARD_SCHEDULE = data['credit_card_schedule']
DAYS_IN_ADVANCE = data["credit_card_days_in_advance"]


def cc_alert():
    """
    Sends an alert a few days in advance of the mortgage due dates.
    """
    today = datetime.date.today()

    # Days in advance to send the alert (e.g., 3 days before the due date)
    days_in_advance = DAYS_IN_ADVANCE

    body = ""

    # Loop through the mortgage schedule to check upcoming due dates
    for entry in CREDIT_CARD_SCHEDULE:
        due_day = entry["due_day"]  # Day of the month
        account = entry["account_name"]
        # Get today's date and construct the due date
        due_date = datetime.date(today.year, today.month, due_day)

        # If the due date is in the current month and it's within the advance period, send alert
        if today <= due_date and (due_date - today).days <= days_in_advance:
            body += (
                f"Reminder: The credit card payment for {account} is due on {due_date.strftime('%B %d, %Y')}.\n"
            )

    return body
            
if __name__ == "__main__":
    print(cc_alert())