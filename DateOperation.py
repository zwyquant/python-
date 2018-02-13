from datetime import datetime,timedelta

def DateOperation(): 
    a = datetime(2018,2,8)
    
    b = datetime(2017,12,13)
    c = a + timedelta(days=54) #求指定日期54天以后的日期

    now = datetime.today() #获取当前时间
    d = now + timedelta(minutes=10) #从当前时间开始10分钟后的时间
    e = (a-b).days #两个日期相差多少天
  
    print (c,d,e, sep='\n')



def main():
    DateOperation() 
 

if __name__ =='__main__':
    main()
