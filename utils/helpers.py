from datetime import datetime

def get_current_hour():
    return datetime.now().hour

def greet():
    hour = get_current_hour()
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
