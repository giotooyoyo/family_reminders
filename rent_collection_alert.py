import datetime
import json

file_path = "personal_data.json"
with open(file_path, 'r') as file:
    data = json.load(file)
RENT_COLLECTION_SCHEDULE = data['rent_collection_schedule']

def rent_collection_alert():
    today = datetime.date.today()

    for entry in RENT_COLLECTION_SCHEDULE:
        rent_day = entry['due_day']
        tenant_name = entry['tenant_name']
        amount_due = entry['amount_due']

        # If today matches the rent collection day
        if today.day == int(rent_day):
            body = f"Reminder: Rent is due today for {tenant_name}. Amount: ${amount_due}. Please check the rent."
            return body
    
    return " "
        
