from collections import defaultdict
import datetime
import json

file_path = "personal_data.json"
with open(file_path, 'r') as file:
    data = json.load(file)
MORTGAGE_SCHEDULE = data['mortgage_schedule']
DAYS_IN_ADVANCE = data["mortgage_days_in_advance"]

def mortgage_alert():
    """
    Sends an alert a few days in advance of the mortgage due dates.
    """
    today = datetime.date.today()

    # Days in advance to send the alert (e.g., 3 days before the due date)
    days_in_advance = DAYS_IN_ADVANCE

    body = ""

    # Loop through the mortgage schedule to check upcoming due dates
    for entry in MORTGAGE_SCHEDULE:
        due_day = entry['due_day']  # Day of the month
        tenant_name = entry['tenant_name']
        amount_due = entry['amount_due']
        checking_account = entry['checking_account']
        # Get today's date and construct the due date
        due_date = datetime.date(today.year, today.month, due_day)

        # If the due date is in the current month and it's within the advance period, send alert
        if today <= due_date and (due_date - today).days <= days_in_advance:
            body += (
                f"Reminder: The mortgage payment for {tenant_name} is due on {due_date.strftime('%B %d, %Y')}.\n"
                f"Amount: ${amount_due}.\n"
                f"Please ensure you have sufficient funds in your {checking_account} account.\n"
            )

    return body
            
if __name__ == "__main__":
    print(mortgage_alert())