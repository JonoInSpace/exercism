from datetime import datetime, date
from calendar import monthrange

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    WEEKS = ['teenth', '1st', '2nd', '3rd', '4th', '5th', 'last']
    
    assert month in range(1,13), 'That\'s not a month!'
    
    if day_of_week in WEEKDAYS:
        weekday_index = WEEKDAYS.index(day_of_week) + 1
    else:
        raise MeetupDayException('That\'s not a weekday!')
    
    if week in WEEKS:
        week_index = WEEKS.index(week)
    else:
        raise MeetupDayException('That\'s not a week!')
    
    if week_index not in (0, 6):  # first - fifth
        count = 0 
        for i in range(1, monthrange( year, month )[1] + 1):
            if date(year, month, i).isoweekday() == weekday_index:
                 count += 1
            if count == week_index:
                return date(year, month, i)
        raise MeetupDayException(f'no {week} {day_of_week} of month')
            
    elif week_index == 6: # last
        for i in range(monthrange(year, month)[1], 0, -1):
            if date(year, month, i).isoweekday() == weekday_index:
                return date(year, month, i)

            
    elif week_index == 0: # teenth
        for i in range(13, 20):
            if date(year, month, i).isoweekday() == weekday_index:
                return date(year, month, i)