def add_time(*args):
    HOURS_DAY = 24
    HOURS_WEEK = 168
    MINUTES_DAY = 1440
    MINUTES_WEEK = 10080
    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start = args[0]
    duration = args[1]
    weekday = args[2].capitalize()
    weekday_pos = WEEKDAYS.index(weekday)
    
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
    if sum_minutes > MINUTES_DAY:
        days = int((sum_minutes / MINUTES_DAY))
        #print ("days: ", days)
    new_time = ""

    # Display new time if it is still the same day
    if days==0: 
        if sum_minutes < MINUTES_DAY/2:
            print(daytime)
            daytime = "AM"
            if sum_minutes%60 != 0:
                new_hours = int((sum_minutes - (sum_minutes % 60)) / 60)
                new_minutes = sum_minutes % 60
            else:
                new_hours = int(sum_minutes / 60)
                new_minutes = 0
            
            if new_minutes < 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + weekday
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + weekday
        else:
            daytime = "PM"
            #print(daytime)
            if sum_minutes%60 != 0:
                new_hours = int((sum_minutes - (sum_minutes % 60)) / 60)-12
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = sum_minutes % 60
            else:
                new_hours = int(sum_minutes / 60)-12
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = 0
            
            # keep the double digit format if minutes are less than 10
            if new_minutes < 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + weekday
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + weekday
        return new_time
    
    # Display the time if the new time is on the next day or more
    else: 
        new_weekday_pos = weekday_pos + days
        if new_weekday_pos < 7:
            new_weekday = WEEKDAYS[new_weekday_pos]
        else:
            new_weekday_pos = int((days%7))
            new_weekday = WEEKDAYS[new_weekday_pos]

        rem_minutes = sum_minutes % MINUTES_DAY
        # print("rem_minutes: ", str(rem_minutes))
        if rem_minutes <=(MINUTES_DAY/2):
            daytime = "AM"
            if rem_minutes % 60 != 0:
                new_hours = int((rem_minutes - (rem_minutes % 60)) / 60)
                new_minutes = rem_minutes % 60
                # print ("new_minutes: ", new_minutes, type(new_minutes))
            else:
                new_hours = int(rem_minutes / 60)
                new_minutes = 0
                
            if new_minutes < 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + new_weekday
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + new_weekday

            # print ("new time: ", new_time)

        else:
            daytime = "PM"
            if rem_minutes % 60 != 0:
                new_hours = int((rem_minutes - (rem_minutes % 60)) / 60)-12
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = rem_minutes % 60
            else:
                new_hours = int(rem_minutes / 60)-12
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = 0
            
            # keep the double digit format if minutes are less than 10
            if new_minutes< 10:
                new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + new_weekday
            else:
                new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + new_weekday
        
        if days < 2:
            return new_time + " (next day)"

        else:
            return new_time + " (" + str(days) + " days later)"

    

# print(add_time("3:00 PM", "3:10"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("6:30 PM", "205:12"))
#print(add_time("11:30 AM", "192:32", "mOnDay"))
#print (add_time("11:43 PM", "24:20", "tueSday"))