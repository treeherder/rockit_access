from twilio.rest import TwilioRestClient
from pymongo import MongoClient
import json

class Txtr():
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




