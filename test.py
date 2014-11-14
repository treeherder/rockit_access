from engine import Calendar
from datetime import datetime
c = Calendar()
y = c.list_numbers()  #a list of tuples of that are (start , end) tuples of (date, time) tuples
#( (start date,  start time), (end date, end time) ) 

#print y[0], len(y), type(y[0][0][0])
#a_date,a_time = (y[0][0][0], y[0][0][1])
#date_format = "%Y-%m-%d %H:%M:%S"
#time_obj = datetime.strptime("{0} {1}".format(a_date, a_time), date_format)
#print time_obj