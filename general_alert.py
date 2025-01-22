import json
from datetime import datetime

# Path to your JSON file
file_path = 'personal_data.json'

# Open and load the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Print the data to verify it's loaded correctly
print(data)

# Accessing data within the JSON structure
today = datetime.today().date()

# Function to check and alert on due tasks
def check_general_schedule():
    reminder_message = ""
    # Loop through each task in the general schedule
    for task in data["general_schedule"]:
        # Parse the due date string into a datetime object
        due_date = datetime.strptime(task["due_day"], "%Y-%m-%d").date()
                
        # Check if the task is due today
        if today <= due_date and (due_date - today).days <= task['days_in_advance']:
            # Send alert (e.g., print reminder)
            reminder_message += (
                f"Reminder: The following task is due {due_date}:\n"
                f"Description: {task['description']}\n"
                f"Amount Due: {task['amount_due'] if task['amount_due'] is not None else 'Not specified'}\n"
                f"Account: {task['account'] if task['account'] is not None else 'Not specified'}\n"
                f"Due Date: {due_date}\n"
            )
    return reminder_message


if __name__ == "__main__":
    check_general_schedule()