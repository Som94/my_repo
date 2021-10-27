
import pandas as pd
import calendar


holidays=pd.read_csv('E:\Aroha Tech\Data Platform\ETL\holidays.csv')

#print(holidays)

shift_type=pd.read_csv('E:\Aroha Tech\Data Platform\ETL\shift_type.csv')
#print(shift_type)


def shift_population(mm,yy):
    try:
    #if mm>=1 or mm<=12:
        date=calendar.month(yy,mm)
        
        split_date=date.split( )
        #print(split_date)
        
        mm=split_date[0][:3]
        
        filename='shift_'+str(mm)+'_'+str(yy)+'.csv'
        #print(filename)
        count=1
        
        for i in split_date[9:]:
            #print(i)
            if len(i)<2:
                i='0'+i
            date_of_month='-'.join((str(i),str(mm),str(yy)))
            #print(date_of_month)
            if date_of_month not in holidays["Date"].values:
                #print ("Ture")
                #print(date_of_month)
                weekday=pd.Timestamp(date_of_month)
                #print(weekday.day_name())
                
               
                if weekday.day_name() != 'Sunday':
                    if weekday.day_name() == 'Saturday':
                        
                       morn_shift=pd.DataFrame({'shift_id' : count,'date':date_of_month,'start_time':shift_type.iloc[0][1],'end_time':shift_type.iloc[0][2]},
                                                   columns = ['shift_id','date','start_time','end_time'],index=[0]) 
                      
                       count += 1
                       morn_shift.to_csv(filename, index=False, sep=',' , mode='a', header=False)
    
                    
                    else:
                        morn_shift=pd.DataFrame({'shift_id' : count,'date':date_of_month,'start_time':shift_type.iloc[0][1],'end_time':shift_type.iloc[0][2]},
                                                   columns = ['shift_id','date','start_time','end_time'],index=[0]) 
                        count += 1
                        morn_shift.to_csv(filename, index=False, sep=',', mode='a', header=False)
    
                        
                        aftrn_shift=pd.DataFrame({'shift_id' : count,'date':date_of_month,'start_time':shift_type.iloc[1][1],'end_time':shift_type.iloc[1][2]},
                                                   columns = ['shift_id','date','start_time','end_time'],index=[1]) 
                        count += 1
                        aftrn_shift.to_csv(filename, index=False, sep=',', mode='a', header=False)
    
    except:
        print("\n Enter a valid month between 1 to 12 only..")
    
mm=int(input("Enter a month between 1-12 :"))
yy=int(input("Enter year  :"))
        
shift_population(mm,yy)
