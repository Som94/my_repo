'''
1) d1 = '12/05/2020'
It is in dd/mm/yyyy format
Which weekday is it?
How many days have elapsed from that date to the current date?
'''
from datetime import date
import datetime

import calendar

def week_day(yyyy,mm,dd):
    
    if year%400==0 or year%100!=0 and year%4==0:
        if month==2:
            if day>0 and day<30:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print("It's a leap year, so 2nd month date should be in 1 to 29 ")
            
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if day>0 and day<=31:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print(" month date should be in 1 to 31 ")
        elif month==4 or month==6 or month==9 or month==11:
            if day>0 and day<=30:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print(" month date should be in 1 to 30 ")
        else:
            print("Plz , Enter month between 1 to 12")
            
    
    else:
        
        if month==2:
            if day>0 and day<29:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print("It's not a leap year, so 2nd month date should be in 1 to 28 ")
            
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if day>0 and day<=31:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print(" month date should be in 1 to 31 ")
        elif month==4 or month==6 or month==9 or month==11:
            if day>0 and day<=30:
                Fdate=datetime.date(year,month,day)
                Fday=Fdate.strftime('%A')
                print(Fday)
                
            else:
                print(" month date should be in 1 to 30 ")
        else:
            print("Plz , Enter month between 1 to 12")
            
        
        
    

year=int(input("Enter the Year : "))
month=int(input("Enter the Month : "))
day=int(input("Enter the Day : "))

week_day(year,month,day)
