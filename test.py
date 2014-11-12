from engine import Calendar
from datetime import datetime
c = Calendar()
y = c.list_timeslots()
a_date,a_time = (y[0][0][0], y[0][0][1])
date_format = "%Y-%m-%d %H:%M:%S"
time_obj =  = datetime.strptime("{0} {1}".format(a_date, a_time), date_format)
print t