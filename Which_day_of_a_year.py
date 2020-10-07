# given a date, check it is on which day of the year

days_month_leap = [31,29,31,30,31,30,31,31,30,31,31,30]
days_month_non_leap = [31,28,31,30,31,30,31,31,30,31,31,30]

def which_day (year,month,day):
    days = 0
    if (year%4==0) & (year%100 != 0) | (year%400 == 0):
        for i in range(month-1):
            days += days_month_leap[i]
        days += day
    else:
        for i in range(month-1):
            days += days_month_non_leap[i]
        days += day
    return days

d = which_day(2020,8,7)
print(d)
