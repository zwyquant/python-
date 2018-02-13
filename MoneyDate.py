from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7 
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def main():
    today = datetime.today()
    a = get_previous_byday('Monday') #求上一个星期一对应的日期.
    t=datetime.strptime(str(a)[0:10], "%Y-%m-%d").date()

    b = get_previous_byday('Monday', datetime(2017,12,28)) #当前日期是2017年12.28日,求上一个星期一对应的日期
    t2 = datetime.strptime(str(b)[0:10], "%Y-%m-%d").date()

    print (t)
    print (t2)
 

if __name__ =='__main__':
    main()

