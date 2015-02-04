#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,  pycurl
from engine import Calendar,Txtr
from datetime import datetime, date, timedelta
from pymongo.connection import Connection

conn = Connection("localhost")
db = conn["rockit_access"]
curl_object = pycurl.Curl()
curl_object.setopt(pycurl.URL, "http://www.iobridge.com/widgets/static/id=lcDWU8QO2KJw")

dbup_flag = False  #database updated

t = Txtr()
c = Calendar("Started")
#let people in with http://www.iobridge.com/widgets/static/id=lcDWU8QO2KJw
print (c.list_timeslots())

t_fmt =  "%a, %d %b %Y %H:%M:%S"  #time formating object

def right_now():
  return ( datetime.strptime(datetime.now().strftime(t_fmt),t_fmt))

def chk_msgs():
    recent_messages = []
    #after updating the database, there should be 
    #collection for each number that has attempted to contact us
    #this collection should be full of documents containing
    #user spceific data
    for usr_prf in db.collection_names():
      if "system" not in usr_prf:
        for msgs in  db[usr_prf].find():
          rec_at =  msgs["time"].replace('"', '')[:25]
          d_o = datetime.strptime( rec_at, t_fmt)
          #print d_o 
          delta = right_now() - timedelta(minutes=10)
          if  d_o >= delta:# check to see if message was recd in the last 10 mins or so
             print msgs
    #the time interval is close enough to be valid
     #   recent_messages.append( {'cell':txt_msg['from'], 'msg': txt_msg['body']} )
     #construct JSON object for messages database:
    #return (recent_messages)

t.update_database()
chk_msgs()
print "done"
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
