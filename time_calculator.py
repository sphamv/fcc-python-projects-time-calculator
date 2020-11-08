def add_time(*args):
    MINUTES_DAY = 1440
    MINUTES_WEEK = 10080
    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start = args[0]
    duration = args[1]
    try:
        weekday = args[2].capitalize()
        weekday_pos = WEEKDAYS.index(weekday)
    except:
        weekday = ""
    
    
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
    if d_minutes == 0:
        if len(weekday)>0:
            return start + ", " + weekday
        else:
            return start

    if sum_minutes > MINUTES_DAY:
        days = int((sum_minutes / MINUTES_DAY))
        #print ("days: ", days)
    new_time = ""

    # Display new time if it is still the same day
    if days==0: 
        if sum_minutes < MINUTES_DAY/2:
            daytime = "AM"
            if sum_minutes%60 != 0:
                new_hours = int((sum_minutes - (sum_minutes % 60)) / 60)
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = sum_minutes % 60
            else:
                new_hours = int(sum_minutes / 60)
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = 0
            
            if len(weekday)>0:
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + weekday
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + weekday
            else: 
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime
            
        else:
            daytime = "PM"
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
            if len(weekday)>0:
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + weekday
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + weekday
            else: 
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime
        return new_time
    
    # Display the time if the new time is on the next day or more
    else: 
        try: 
            new_weekday_pos = weekday_pos + days
            if new_weekday_pos < 7:
                new_weekday = WEEKDAYS[new_weekday_pos]
            else:
                new_weekday_pos = ((weekday_pos + days)%7)
                print(new_weekday_pos)
                new_weekday = WEEKDAYS[new_weekday_pos]
        except: 
            new_weekday = ""
        rem_minutes = sum_minutes % MINUTES_DAY
        # print("rem_minutes: ", str(rem_minutes))
        if rem_minutes <=(MINUTES_DAY/2):
            daytime = "AM"
            if rem_minutes % 60 != 0:
                new_hours = int((rem_minutes - (rem_minutes % 60)) / 60)
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = rem_minutes % 60
                # print ("new_minutes: ", new_minutes, type(new_minutes))
            else:
                new_hours = int(rem_minutes / 60)
                if new_hours == 0: #display 12 pm instead of reverting to 0
                    new_hours +=12
                new_minutes = 0

            if len(weekday)>0:    
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + new_weekday
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + new_weekday
            else: 
                if new_minutes < 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime
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
            if len(weekday)>0:
                if new_minutes< 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime + ", " + new_weekday
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime + ", " + new_weekday
            else: 
                if new_minutes< 10:
                    new_time = str(new_hours) + ":" + "0" + str(new_minutes) + " " + daytime
                else:
                    new_time = str(new_hours) + ":" + str(new_minutes) + " " + daytime

        
        if days < 2:
            return new_time + " (next day)"

        else:
            return new_time + " (" + str(days) + " days later)"

    

#print(add_time("11:06 PM", "2:02"))
# print(add_time("11:43 AM", "00:20"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("6:30 PM", "205:12"))
# print(add_time("11:30 AM", "192:32", "mOnDay"))
#print (add_time("11:43 PM", "24:20", "tueSday"))

#print(add_time("5:01 AM", "0:00"))
#print(add_time("8:16 PM", "466:02", "tuesday"))

#print(add_time("11:59 PM", "24:05", "Wednesday"))