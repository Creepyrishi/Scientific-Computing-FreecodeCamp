def add_time(start, duration, dayName=None):
      week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
      Time, initialState = start.split(" ")
      initialHour, initialMin = Time.split(":")
      if initialState == "PM":
            initialHour = int(initialHour) + 12
      durHour, durMin = duration.split(":")
      tempMin = int(durHour)*60 +int(initialHour) *60 + int(initialMin) + int(durMin)
      totalHour = (tempMin)//(60)
      days = totalHour // 24
      if days == 1:
            dayCaption = " (next day)"
      elif days == 0:
            dayCaption = ''
      else:
            dayCaption = f" ({days} days later)"
      newHour = int(totalHour) - days*(24)
      if newHour == 12:
            newState = "PM"
      elif newHour > 12:
            newHour = newHour - 12
            newState = "PM"
      elif newHour == 0:
            newHour = 12
            newState = "AM"
      else:
            newState = "AM"
      newMin = tempMin - totalHour*60
      if len(str(newMin)) < 2:
            newMin = "0" + str(newMin)
      
      if dayName == None:
            time = f"{newHour}:{newMin} {newState}{dayCaption}"
      else:
            dateIndex = days + week.index(dayName.lower())+1
            newDayIndex = dateIndex % 7
            day = week[newDayIndex-1].capitalize()
            time = f"{newHour}:{newMin} {newState}, {day}{dayCaption}"
      
      return time
