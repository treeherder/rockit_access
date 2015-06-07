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
args = parser.parse_args()


def right_now():
#a simple method to handle datetime objects
  return ( datetime.strptime(datetime.now().strftime(t_fmt),t_fmt))


class Handler():
#this class exists to interface between the various data systems and the frontend
#when the program is called, this class should spawn an instance that coresponds to a user session

  def __init__(self, user, handler_id, status="Started"):
    self.user = user
    self.handler_id = handler_id  #id of the user session
    self.text = Txtr()
    self.events = Calendar(status) #going to have to parse these out, event by event

  def check_events(self):
    print type(self.events.list_timeslots())
    print (self.events.list_timeslots())

    #check if there are times listed for an event "right now"

    if len(self.events.list_timeslots()) <=0:
      return (False)
    else:
      return(True)



#procedural bits... just for testing for the moment

if args.set_status:
  h = Handler(args.user, args.handler_id, args.status)
else:
  h = Handler(args.user, args.handler_id)

print(h.check_events())
