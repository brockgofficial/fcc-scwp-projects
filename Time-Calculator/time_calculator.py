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

# TODO
# - don't need to add checks to validate input
# - assume start times are valid times
# - minutes in duration is 0 - 60 mins
# - hour can be any whole number
# - Outputs can be:
#   - Combined time
#   - Combined time, Day
#   - Combined time, (next day/# days later)
#   - Combined time, Day (next day/# days later)

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
  if days_passed == 1:
    days_passed = ", (next day)"
  elif days_passed >= 2:
    days_passed = ", ({} days later)".format(days_passed)
  else:
    days_passed = ""

  #Display the new time output (including Day/Extra Days if applicable)
  new_time_proto = "Orig(m): {} - New(m): {} - Days Passed: {}".format(h_start * 60 + m_start , t_new, int(t_new / (24*60)))
  new_time = "{:02d}:{:02d} {}M{}".format(12 if h_new == 0 else h_new, m_new, "A" if h_new < 12 else "P", days_passed)

  return new_time