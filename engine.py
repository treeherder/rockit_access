#!/usr/bin/python
# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
from pymongo import MongoClient
from eb_api_handler import *
import json, datetime

class Txtr(): #twilio is straightforward and does not need complicated wrappers
  def __init__(self):
    self.twil = TwilioRestClient(twil_auth["sid"], twil_auth["token"])
    self.mc = MongoClient()
    self.db = self.mc["rockit_access"]


  def send_text(self, message, rec):
    sms = self.twil.messages.create(body=message,
                                      to=rec,
                                      from_="15102545456")

  def get_texts(self):
    messages = []
    for message in self.twil.messages.list(to ="15102545456"):
      messages.append( {"body":message.body, "sent":message.date_sent, "from":message.from_} )
    return (messages)

  def filter_texts(self, list_of_msgs, filter):
    #filter text for recent time stamp
    #see texts from filter subject
    #see what they sent most recently
    #look for something like "let me in" & relevant time r
    msgs = []
    for msg in list_of_msgs:
      if filter in msg["from"]:
         msgs.append((msg["body"], msg["sent"]))
    return msgs

  def update_database(self):
    c_s = []
    c_l = []
    for msg in self.get_texts():
      c_l.append(msg["from"])
    s_set = set(c_l)
    #create a set of all numbers from which to name the collections:
    for nbr in s_set:
      client_collection = json.dumps(nbr)
      c_s.append(client_collection.replace('"', '').strip("+"))
    for c in set(c_s):
      for itm in self.filter_texts(self.get_texts(), c):
        self.db[c].save({"time":json.dumps(itm[1]), "msg":json.dumps(itm[0])}, w=0)
        #print({"time":json.dumps(itm[1]), "msg":json.dumps(itm[0])})
        self.db[c].ensure_index("time", unique =True)


class Calendar(): #handle eb API
  def __init__(self, status):
    self.today = datetime.date.today().strftime("%Y-%m-%d")  #format date for EB output
    self.status = status

  def list_timeslots(self): #returns list of timeslot tuples
    timeslots = []
    for events in touch_events(self.status):
      date_format = "%Y-%m-%d %H:%M:%S"
      start_time_obj = datetime.datetime.strptime("{0}".format(events["start"]), date_format)
      #print start_time_obj
      end_time_obj = datetime.datetime.strptime("{0}".format(events["end"]), date_format)
      #print end_time_obj
      timeslots.append( (start_time_obj, end_time_obj) )
    return (timeslots)

  def check_number(self, number):  #iterate over a list of guest tuples
    for listing in authorize_user(touch_events(self.status))["allowed"] :
      if number in listing["phone"]:
        return (True)
      else:
        return (False)

  def check_email(self, email):  #iterate over a list of guest tuples
    for listing in authorize_user(touch_events(self.status))["allowed"]:
      if email in listing:
        return (True)
    for listing in auOBthorize_user(touch_events(self.status))["Denied"]:
      if email in listing:
        return (True)
    return (False)


  def print_attendee_data(self):
    for event in touch_events(self.status):
      print (event["id"])
      try:
        print(authorize_user(event))
      except:
        print ("done")
