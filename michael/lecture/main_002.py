
#Task 5
# Produce days of Week
def get_day(day):
    if day == "Monday":
        return f'The day of the Week is: {day}'
    elif day == "Tuesday":
        return "Tuesday"
    elif day == "Wednesday":
        return "Wednesday"
    elif day == "Thursday":
        return "Thursday"
    elif day == "Friday":
        return "Friday"
    elif day == "Saturday":
        return "Saturday"
    elif day == "Sunday":
        return "Sunday"
    else:
        return "Invalid day inputr"
print(get_day("Monday"))
    

