###
# Function to define how to calculate time
#
# - Args:
#   - start: Start time in 12-hour format ending in AM or PM.
#   - duration: A duration in hours and minutes.
#   - day: A starting day of the week, case insensitive (optional).
#
# - Return:
#   - new_time, The start time with the added duration.
###

def add_time(start, duration, day=False):

  #Split starting time into parts
  h_start, m_start = map(int, start[:-2].split(':'))
  h_start %= 12
  if start[-2:] == 'PM':
    h_start += 12

  #Split duration in parts
  h_duration, m_duration = map(int, duration.split(":"))
  
  #Get new time in minutes
  t_new = h_start * 60 + m_start +  h_duration * 60 + m_duration

  #Convert new time to hours and minutes
  h_new, m_new = divmod(t_new, 60)
  h_new %= 24

  #Calc days passed
  days_passed = int(t_new / (24 * 60))

  #Get the new day (if applicable)
  if day != False:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day = days_of_week.index(day.lower().capitalize())
    new_day =  days_of_week[((current_day - len(days_of_week)) + (days_passed % len(days_of_week)))] if (current_day + days_passed) > len(days_of_week) else days_of_week[current_day + days_passed]
  
  #Formulate final time string, based on the days passed
  if days_passed == 1:
    days_passed = "{} {}".format("" if day == False else (", " + new_day), "(next day)")
  elif days_passed >= 2:
    days_passed = "{} {}".format("" if day == False else (", " + new_day), "(" + str(days_passed) + " days later)")
  else:
    days_passed = "{}".format("" if day == False else (", " + new_day))

  #Display the new time output (including Day/Extra Days if applicable)
  new_time = "{:01d}:{:02d} {}M{}".format(h_new -12 if h_new > 12 else (12 if h_new == 0 else h_new), m_new, "A" if h_new < 12 else "P", days_passed)

  #Return the new time with the day and passed days if applicable
  return new_time