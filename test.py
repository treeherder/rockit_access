#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, time
from engine import Calendar,Txtr
from datetime import datetime, date, timedelta
from pymongo.connection import Connection

conn = Connection("localhost")
db = conn["rockit_access"]


t = Txtr()
c = Calendar("Started")
#print c.list_timeslots()
#print c.check_number("4014517150")
#print type(t.get_texts())
#print len(t.get_texts())
#print ( t.get_texts()[0] )
t_fmt =  "%a, %d %b %Y %H:%M:%S"  #time formating object



def right_now():
  return ( datetime.strptime(datetime.now().strftime(t_fmt),t_fmt))
def chk_msgs():
    recent_messages = []
    for txt_msg in  t.get_texts():
      rec_at = ( json.dumps(txt_msg["sent"][:25]).strip('"') )
      d_o = datetime.strptime( rec_at, t_fmt) #date object
      delta = right_now() - timedelta(minutes=10) #start a timedelta from 10 mins ago
      if  d_o >= delta:# check to see if message was recd in the last 10 mins or so
        #the time interval is close enough to be valid
        recent_messages.append( {'cell':txt_msg['from'], 'msg': txt_msg['body']} )
     #construct JSON object for messages database:
    return (recent_messages)

def reply_msg():
  t.update_database()  

reply_msg()

#Next step:
# create database of messagesi with a system to flag them for whether or not they have been processed

#print ( chk_msgs())
#for msg in chk_msgs():
#  db.update({"id": chk_msgs  
   #if (d_o < right_now())
    #print datetime.now().strftime(t_fmt)
#if (sent_at  datetime.now().strftime(t_fmt)
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
#Sun, 16. Nov 2014'

   # check time of text message, allow only valid window of a certain period.
   #reply appropriately to text,
#basic reply "sorry you are not listed as an attendee to this event, maybe we missed you...
#allow some kind of user interface to set permissions....
