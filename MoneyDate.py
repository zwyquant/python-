from datetime import datetime,date,timedelta
import time
import calendar

def get_month_range(start_date=None): 
    if start_date is None:
        start_date=date.today().replace(day=1)
        print(start_date,type(start_date))
    _,days_in_month = calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=days_in_month)

    return (start_date,end_date)


def main():
    a_day = timedelta(days=1)

    dtstr = '2018-01-08'
    t=datetime.strptime(dtstr, "%Y-%m-%d").date()
  
    first_day,last_day=get_month_range(t)

    datelist = []
    while first_day < last_day:
        datelist.append(str(first_day))
        first_day += a_day
    print(datelist)


if __name__ =='__main__':
    main()
