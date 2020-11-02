def add_time(start, duration):
    HOURS_DAY = 24
    HOURS_WEEK = 168
    MINUTES_DAY = 1440
    MINUTES_WEEK = 10080
    

    if len(start.split()) !=2 or int(start.split()[0].split(":")[0])>12 or start.split()[1] not in ["AM", "PM"]: 
        return "Error: Invalid starting time format"
    
    if int(duration.split(":")[1])>59:
        return "Error: Invalid duration time format"

    #extract and convert starting time into minutes

    if start.split()[1] == 'AM':
        s_hours = int(start.split()[0].split(":")[0])
        s_minutes = int(start.split()[0].split(":")[1]) + (s_hours * 60)
    else:
        s_hours = int(start.split()[0].split(":")[0]) + 12
        s_minutes = int(start.split()[0].split(":")[1]) + (s_hours * 60)

    d_minutes = int(duration.split(":")[0])*60 + int(duration.split(":")[1])
   
    sum_minutes = s_minutes + d_minutes

    days = 0
    new_time = ""

    # Display new time if it is still the same day
    if sum_minutes < 1440: 
        if sum_minutes < 1440/2:
            daytime = "AM"
            if sum_minutes%60 != 0:
                new_hours = int((sum_minutes - (sum_minutes % 60)) / 60)
                new_minutes = sum_minutes % 60
            else:
                new_hours = int(sum_minutes / 60)
                new_minutes = 0
            
            if new_minutes < 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime
        else:
            daytime = "PM"
            if sum_minutes%60 != 0:
                new_hours = int((sum_minutes - (sum_minutes % 60)) / 60)-12
                new_minutes = sum_minutes % 60
            else:
                new_hours = int(sum_minutes / 60)-12
                new_minutes = 0
            
            # keep the double digit format if minutes are less than 10
            if new_minutes < 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime
    else: 
        return "next day"

    return new_time

print(add_time("12:00 AM", "11:50"))