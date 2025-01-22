
import datetime
from calendar import monthrange



SUBJECT = "Daily Housework Reminder"

# List of housework tasks
housework_tasks = [
    "Bedroom floor cleaning",
    "Bedroom window cleaning",
    "Bathroom cleaning",
    "Kitchen cleaning",
]

bedroom_selection = [
    "Master Bedroom",
    "Katelyn Room",
    "Zoe Room"
]

bathroom_selection = [
    "Master Bathroom",
    "Katelyn & Zoe Bathroom",
    "Powder Room",
    "Basement"
]

kitchen_selection = [
    "Dining table",
    "Fridge",
    "Windows"
]



def task_selection(day, week_of_month, day_of_week):
    # Determining the task for the day depending on week of the month, and day of the week

    # Skip Saturdays (5) and Sundays (6)
    if day_of_week >= 5:
        print(f"Today is {day.strftime('%A')}. No tasks assigned for weekends.")
        return

    # Determine the task for today based on the day of the week
    task_for_today = housework_tasks[week_of_month % len(housework_tasks)]

    # Determine the corresponding location (room or area) based on task type
    location_for_today = ""
    
    if "Bedroom" in task_for_today:
        location_for_today = bedroom_selection[day_of_week % len(bedroom_selection)]
    elif "Bathroom" in task_for_today:
        location_for_today = bathroom_selection[day_of_week % len(bathroom_selection)]
    elif "Kitchen" in task_for_today:
        location_for_today = kitchen_selection[day_of_week % len(kitchen_selection)]

    # Print the task and the corresponding location for today
    return f"Task for {day} ({day.strftime('%A')}): {task_for_today} in the {location_for_today}"


def print_month_schedule():
    # Get the current month and year
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Determine the number of days in the current month
    num_days_in_month = monthrange(year, month)[1]

    # Print out the schedule for this month
    print(f"Housework Schedule for {today.strftime('%B %Y')}:")
    print("=" * 40)

    # Loop through all days in the current month
    for day in range(1, num_days_in_month + 1):
        # Create a date object for each day in the month
        current_day = datetime.date(year, month, day)

        # Get the day of the week (0 = Monday, 6 = Sunday)
        day_of_week = current_day.weekday()

        # Calculate the week of the month (1st week = 1, 2nd week = 2, etc.)
        week_of_month = (day - 1) // 7 + 1

        # Call task_selection to assign tasks
        task_selection(current_day, week_of_month, day_of_week)

def today_task():
    today = datetime.date.today()
    day_of_week = today.weekday()
    day_of_month = today.day
    week_of_month = (day_of_month - 1) // 7 + 1
    return task_selection(today, week_of_month, day_of_week)


# Schedule the task to send the email every day at 8:00 AM
# schedule.every().day.at("08:00").do(create_daily_task_email)

# Keep the script running to maintain the schedule
#while True:
#    schedule.run_pending()
#    time.sleep(60)  # Wait 1 minute between checks

if __name__ == "__main__":
    

    # Get the day of the week (0 = Monday, 6 = Sunday)
    today_task()
    # create_daily_task_email()
    print_month_schedule()