from datetime import datetime
import math
now = datetime.now()
hours = now.strftime("%H")
minutes = now.strftime("%M")
print("Now:")
print(hours+ ":"+ minutes)


##SYDNEY
SYD = 270
CT = int(hours) * 60 + int(minutes)
SYDt = (CT + SYD)
SYDH = SYDt // 60
SYDM = SYDt % 60
print("                                                                                                ")
print("Sydney:")

if SYDH == 24:
    SYDh = 12

if SYDH >= 24:
    SYDHn = SYDH - 24

if SYDM < 10:
    SYDMn = str(SYDM).zfill(2)

if SYDH == 24 and SYDM < 10:
    print(str(SYDh)+ ":"+ str(SYDMn)+ " AM")

if SYDH == 24 and SYDM > 10:
    print(str(SYDh)+ ":"+ str(SYDM)+ " AM")

if SYDH > 24 and SYDM < 10:
    print(str(SYDHn)+ ":"+ str(SYDMn)+ " AM")

if SYDH > 24 and SYDM > 10:
    print(str(SYDHn)+ ":"+ str(SYDM)+ " AM")

if SYDH < 24 and SYDM < 10:
    print(str(SYDH)+ ":"+ str(SYDMn)+ "PM")

if SYDH < 24 and SYDM > 10:
    print(str(SYDH)+ ":"+ str(SYDM)+ "PM")

