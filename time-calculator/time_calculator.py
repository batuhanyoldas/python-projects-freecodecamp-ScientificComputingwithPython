def add_time(start, *duration):

  end_ampm = ""
  end_day = ""
  days_later = ""
  start_day = ""
  week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  is_start_day_given = 0

  if len(duration) == 2:
    is_start_day_given = 1
    start_day = duration[1]
  
  start_time_ampm = start.split(" ")
  start_hour_min = start_time_ampm[0].split(":")
  start_hour = start_hour_min[0]
  start_min = start_hour_min[1]
  start_ampm = start_time_ampm[1]

  duration_hour_min = duration[0].split(":")
  duration_hour = duration_hour_min[0]
  duration_min = duration_hour_min[1]

  end_hour = int(start_hour) + int(duration_hour)
  end_min = int(start_min) + int(duration_min)

  if end_min != (end_min%60):
    end_hour += 1
  end_min = str(end_min%60)

  if len(end_min) == 1:
   end_min = "0"+ end_min

  half_days = end_hour // 12
  full_days = half_days // 2
  if half_days%2 == 0:
    end_ampm = start_ampm
  else:
    if start_ampm == "AM":
      end_ampm = "PM"
    else:
      end_ampm = "AM"
      full_days += 1
      
  if full_days == 1:
    days_later = " (next day)"
  elif full_days > 1:
    days_later = " (" + str(full_days) + " days later)"
    
  full_days = full_days%7
  if is_start_day_given == 1:
    i = 0
    for day in week_days:
      if start_day.upper() == day.upper():
        break
      else:
        i += 1
    #end_day = week_days[i+full_days]
    i = (i+full_days) % 7
    end_day = ", " + week_days[i]
  end_hour = end_hour % 12
  if end_hour == 0:
    end_hour = 12

  new_time = str(end_hour) + ":" + str(end_min) + " " + end_ampm + end_day + days_later
  return new_time