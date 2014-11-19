from engine import Calendar,Txtr
from datetime import datetime
t = Txtr("test","rockit")
c = Calendar()
y = c.check_number("4014517150") #a list of tuples of that are (start , end) tuples of (date, time) tuples
#( (start date,  start time), (end date, end time) ) 
print t.filter_texts(t.get_texts(), "4014517150")
#print y 

#print y[0], len(y), type(y[0][0][0])
#a_date,a_time = (y[0][0][0], y[0][0][1])
#date_format = "%Y-%m-%d %H:%M:%S"
#time_obj = datetime.strptime("{0} {1}".format(a_date, a_time), date_format)
#print time_obj
#dt = datetime.datetime.strptime( datetime.date.today().strftime("%Y/%m/%d"), "%Y/%m/%d")
#dt
#datetime.datetime(2014, 11, 16, 0, 0)
#print dt
#2014-11-16 00:00:00
#datetime.datetime.strftime(dt, "%a, %d. %b %Y") 
#'Sun, 16. Nov 2014'
