from twilio.rest import TwilioRestClient
from pymongo import MongoClient
from eb_api_handler import *
import json, datetime

class Txtr(): #twilio is straightforward and does not need complicated wrappers
  def __init__(self, db_name, col_name):
    self.client = MongoClient()
    self.db = self.client[db_name]
    self.col = self.db[col_name]
    self.profile = self.col.find_one({"name": db_name})
    self.twil = TwilioRestClient(self.profile["sid"], self.profile["token"])
    print(self.profile["sid"], self.profile["token"])
  

  def send_text(self, message, rec):
    sms = self.twil.messages.create(body=message,
                                      to=rec,
                                      from_="15102545456")
  def get_texts(self):
    for message in self.twil.messages.list(to ="15102545456"):
      print message.body
      print message.date_sent
      print message.from_


class Calendar(): #handle eb API
  def __init__(self):
    self.today = datetime.date.today().strftime("%Y-%m-%d")  #format date for EB output
  
  def list_timeslots(self): #returns list of timeslot tuples
    timeslots = []
    print touch_events()[0]
    #for timeslot_id in authorize_schedule(touch_events()['id']):
     # print timeslot_id
      #timeslots.append(timeslot[0:])
    #return timeslots

  #def validate_timeslot(self, timeslots):
    