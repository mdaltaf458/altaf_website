from datetime import date
import calendar
s,e=input("Enter startdate: "),input("Enter Enddate: ")
Year,eYear=s[0:4],e[0:4]
sm,em=s[5],e[5]
Year,eYear=int(Year),int(eYear)
sm,em=int(sm),int(em)
l=em

if(em<=sm):
    em=12
A=calendar.TextCalendar(calendar.SATURDAY)
print("\n")
print("The Output is")

for b in range(sm,em+1):
    c=0
    for k in A.itermonthdays(Year,b):
        if k!=0:
            day=date(Year,b,k)
            if day.weekday()==5:
                c=c+1
                if(c==4):
                    if(k%5!=0):
                        if(b>9):
                            print("%d%d%d"%(Year,b,k))
                        else:
                            print("%d0%d%d"%(Year,b,k))
                else:
                    if(k%5==0):
                        if(b>9):
                            print("%d%d%d"%(Year,b,k))
                        else:
                            print("%d0%d%d"%(Year,b,k))
                    #print("%s,%d-%d-%d" % (calendar.day_name[5] ,k,b,Year))
if(eYear>Year):
    sm=1
    A=calendar.TextCalendar(calendar.SATURDAY)
    for b in range(sm,l+1):
        c=0
        for k in A.itermonthdays(eYear,b):
            if k!=0:
                day=date(eYear,b,k)
                if day.weekday()==5:
                    c=c+1
                    if(c==4):
                        if(k%5!=0):
                            if(b>9):
                                print("%d%d%d"%(eYear,b,k))
                            else:
                                if(k<9):
                                    print("%d0%d0%d"%(eYear,b,k))
                                else:
                                    print("%d0%d%d"%(eYear,b,k))
                    else:
                        if(k%5==0):
                            if(b>9):
                                print("%d%d%d"%(eYear,b,k))
                            else:
                                if(k<9):
                                    print("%d0%d0%d"%(eYear,b,k))
                                else:
                                    print("%d0%d%d"%(eYear,b,k))
                                    
                                    
                                    
