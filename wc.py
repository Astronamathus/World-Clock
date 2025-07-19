from datetime import datetime
import math
now = datetime.now()
hours = now.strftime("%H")
minutes = now.strftime("%M")
print("Now:")
print(hours+ ":"+ minutes)
#import math

#SAN FRANCISCO
SFO_hours = int(hours) - 12
SFO_mins = int(minutes) - 30

if SFO_mins <= 0:
    SFO_mins_n = 00
    SFO_hours_newf = SFO_hours - 1
    SFO_mins_dif = 60 - SFO_mins
    SFO_mins_new = SFO_mins_dif + SFO_mins_n
    print("SFO")
    print(str(SFO_hours_newf)+ ":" +str(SFO_mins_new))

if SFO_hours >= 0:
    SFO_hours_n = 00
    SFO_hours_dif = 24 - SFO_hours
    SFO_hours_new = SFO_hours_dif + SFO_hours_n
    SFO_mins_n = 00
    SFO_hours_newf = SFO_hours - 1
    SFO_mins_dif = 60 - SFO_mins
    SFO_mins_new = SFO_mins_dif + SFO_mins_n
    print("SFO")
    print(str(SFO_hours_new)+ ":" +str(SFO_mins_new))


#SYDNEY

# OVEF code start---
SYD = 330
CT = int(hours) * 60 + int(minutes)
CT1 = (CT + SYD) / 60
SYDH = CT1 - 24
SYDHn = (CT1 - 24) // 1
SYDM = (SYDH % 1) * 60
#print(" ----  OVEF SYD -----")
print(CT)
print(CT1)
print("SYDNEY TIME:" )
print(SYDHn)
print(SYDM)
#print(" ----  OVEF SYD -----")

# OVEF code end---

SYD_hours = int(hours) + 5
SYD_mins = int(minutes) + 30
if SYD_hours >= 24 and SYD_mins >=60:
        SYD_mins_dif = SYD_mins - 60
        SYD_mins_new = SYD_mins_dif
        SYD_hours_dif = SYD_hours - 24
        #SYD_hours_new = SYD_hours_new
        #SYD_hours_new_f = SYD_hours_new + 1
        #print("______________ SYDNEY 1 ______________")
        #print(str(SYD_hours_new_f)+ ":" +str(SYD_mins_new))

if SYD_hours >= 24 or SYD_mins >=60:

    if SYD_hours >= 24:
        SYD_hours_n = 00
        SYD_hours_dif = SYD_hours - 24
        SYD_hours_new = SYD_hours_dif + SYD_hours_n
        print("______________ SYDNEY 2 ______________")
        print(str(SYD_hours_new)+ ":" +str(SYD_mins))

    if SYD_mins >= 60:
        SYD_mins_n = 00
        SYD_hours_new_f = SYD_hours + 1
        SYD_mins_dif = SYD_mins - 60
        SYD_mins_new = SYD_mins_dif + 0 + SYD_mins_n
        print("______________ SYDNEY 3 ______________")
        print(str(SYD_hours_new_f)+ ":" +str(SYD_mins_new))

else:
    print("______________ SYDNEY 4 ______________")
    print(str(SYD_hours)+ ":"+ str(SYD_mins))





#TOKYO
TYO_hours = int(hours) + 3
TYO_mins = int(minutes) + 30

if TYO_hours >= 24 and TYO_mins >=60:
        TYO_mins_n = 00
        TYO_mins_dif = TYO_mins - 60
        TYO_mins_new = TYO_mins_dif + 0 + TYO_mins_n
        TYO_hours_n = 00
        TYO_hours_dif = TYO_hours - 24
        TYO_hours_new = TYO_hours_dif + TYO_hours_n
        TYO_hours_new_f = TYO_hours_new + 1
        print("______________ TOKYO 1 ______________")
        print(str(TYO_hours_new_f)+ ":" +str(TYO_mins_new))

if TYO_hours >= 24 or TYO_mins >= 60:
    TYO_hours_n = 00
    TYO_hours_dif = TYO_hours - 24
    TYO_hours_new = TYO_hours_dif + TYO_hours_n
    TYO_mins_n = 00
    TYO_hours_new_f = TYO_hours + 1
    TYO_mins_dif = TYO_mins - 60
    TYO_mins_new = TYO_mins_dif + 0 + TYO_mins_n
    print("______________ TOKYO 2 _______________")
    print(str(TYO_hours_new)+ ":" +str(TYO_mins_new))

else:
    print("______________ TOKYO 3 ______________")
    print(str(TYO_hours)+ ":"+ str(TYO_mins))







