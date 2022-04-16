def date(start_date):
    
    calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day, month, year = map(int, start_date.split('.'))

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        calendar[1] = 29
    
    if day < calendar[month - 1]:
        day += 1
    else:
        month += 1
        if not month % 3:
            day = 1
        else:
            day = 2

    if month > 12:
        year += 1
        month = 1
    
    new_date = '.'.join(map(lambda x: str(x).zfill(2), (day, month, year)))
    
    return new_date