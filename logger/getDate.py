from datetime import datetime

def getDate():
    today = datetime.now().strftime('%d/%m/%y')
    current_time = datetime.now().strftime('%H:%M:%S')
    now_date = [today, current_time]
    return now_date