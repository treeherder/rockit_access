#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,  pycurl, argparse
from engine import Calendar,Txtr
from datetime import datetime, date, timedelta



parser = argparse.ArgumentParser(description="authorize a user and start a session.  This program is designed to be called as a child process from the node application.")

#group = parser.add_mutually_exclusive_group()
parser.add_argument("-u", "--user", help="the 11 digit phone number of the user we want to route")
parser.add_argument("-S", "--set_status", dest="set_status", action="store_true", help="toggle status from default 'started' parameter" )
parser.add_argument("-s", "--status", dest="status", help="the status of the field of events you wish to query")  #extraneous
parser.add_argument("-f", "--flag", dest="handler_id", action="count", help="set flag for session state")
parser.add_argument("-M", "--include-message", dest="msg_switch", action="store_true", help="flag this field to pass messages")
parser.add_argument("-m", "-message", dest="message", default=[], help="unicode body of the message")

args = parser.parse_args()


t_fmt =  "%a, %d %b %Y %H:%M:%S"  #time formating def

def open_door():
  curl_object = pycurl.Curl()
  curl_object.setopt(pycurl.URL, "http://www.iobridge.com/widgets/static/id=lcDWU8QO2KJw")
  curl_object.perform()
  curl_object.close()



def right_now():
#a simple method to handle datetime objects
  return ( datetime.strptime(datetime.now().strftime(t_fmt),t_fmt))


def num_str(num):
  num = str(num)
  if num[-1] == "1":
    return(num +"st")
  elif num[-1] == "2":
    return(num + "nd")
  elif num[-1] == "3":
    return(num + "rd")
  else:
    return(num + "th")

class Handler():
#this class exists to interface between the various data systems and the frontend
#when the program is called, this class should spawn an instance that coresponds to a user session

  def __init__(self, user, handler_id, status="Started"):
    self.user = user
    self.handler_id = handler_id  #id of the user session
    self.text = Txtr()
    self.events = Calendar(status) #going to have to parse these out, event by event

  def check_events(self):
    print( type(self.events.list_timeslots()))
    print (self.events.list_timeslots())

    #check if there are times listed for an event "right now"
    #if there is NOT an event:
    if len(self.events.list_timeslots()) <=0:
      if (self.handler_id<=1):
        self.text.send_text("I'm sorry, but there are no guests expected at this time. Maybe you should call your host?\r\n  good luck!", self.user)
      elif (self.handler_id>=1):
        self.text.send_text("the time is now:   {0}\r\n and this is now the {1} time you've tried".format(right_now(), num_str(self.handler_id)), self.user)
    else:
      #there is an event
      #check to see if user is authorized for this event
      #maybe just see if it's the daypass event?
      if (self.events.check_number(self.user)):
        open_door()
        self.text.send_text("door opening commenced, welcome to rockit colabs", self.user)
      else:
        if(args.msg_switch):
          for word in args.message.split(" "):
            if "@" in word:
              print(word)
              if(self.events.check_email(word)== True):
                open_door()
                self.text.send_text("welcome to rockit colabs, enjoy your time.", self.user)
              else:
                self.text.send_text("I can't find a record of you registering for this event, I'm sorry.\r\nPurchase a day pass here: rockitcolabs.com/daypass", self.user)
                if "@" not in args.message:
                  self.text.send_text("try sending me your valid registered email", self.user)
                  return(True)



#procedural bits... just for testing for the moment

if args.set_status:
  h = Handler(args.user, args.handler_id, args.status)
else:
  h = Handler(args.user, args.handler_id)
print(h.check_events())
