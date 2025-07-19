import datetime
SYD = 150
NY = 60
GMT = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M")
GMTH = datetime.datetime.now(datetime.timezone.utc).strftime("%H")
GMTM = datetime.datetime.now(datetime.timezone.utc).strftime("%M")
GMTT = int(GMTH) * 60 + int(GMTM)
print("GMT:" +GMT)
print("Available Time Zones: Sydney (syd), New York (NY)")
TZ = input("Your choice:")

##SYDNEY
if TZ in ('SYD', 'syd', 'Sydney', 'sydney'):
    TD_SYD = SYD * 4
    SYDT = TD_SYD + GMTT
    SYDH = SYDT // 60
    SYDM = SYDT % 60

    if SYDH >= 24:
        SYDH = SYDH - 24

    if SYDM < 10:
        SYDM = str(SYDM).zfill(2)

    if SYDH > 24:
        print("Sydney   "+str(SYDH)+ ":"+ str(SYDM)+ " AM️")

    if SYDH < 24:
        print("Sydney   "+str(SYDH)+ ":"+ str(SYDM)+ " PM")

##New York
elif TZ in ('NY', 'ny', 'New York', 'new york'):
        TD_NY = NY * 4
        NYT = GMTT - TD_NY
        NYH = NYT // 60
        NYM = NYT % 60

        if NYH >= 24:
            NYHn = NYH - 24

        if NYM < 10:
            NYMn = str(NYM).zfill(2)

        if NYH > 24 and NYM < 10:
            print("New York   "+ str(NYHn)+ ":"+ str(NYMn)+ " PM️")

        if NYH > 24 and NYM > 10:
            print("New York   "+ str(NYHn)+ ":"+ str(NYM)+ " PM")

        if NYH < 24 and NYM < 10:
            print("New York   "+ str(NYH)+ ":"+ str(NYMn)+ " AM")

        if NYH < 24 and NYM > 10:
            print("New York   "+ str(NYH)+ ":"+ str(NYM)+ " AM")
