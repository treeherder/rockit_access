#!/usr/bin/python
# -*- coding: utf-8 -*-
from secret import *
import json

r = eb.user_list_events()

def touch_events(status):  #returns a list of <status> event dictionaries
  ret_list = []
  for x in xrange(len(r['events'])):  #iterate over the events
    ret={}
    if (r['events'][x]['event']['status'] == status):
      ret['id']=r['events'][x]['event']['id']
      ret['title'] = r['events'][x]['event']['title']
      ret['status'] = r['events'][x]['event']['status']
      ret['start'] = r['events'][x]['event']['start_date']
      ret['end'] = r['events'][x]['event']['end_date']
      ret_list.append(ret)
    #else:  #debug
      #print r['events'][x]['event']['status']
  return (ret_list)

def authorize_schedule(ret_list):  #takes a dictionary  returns a list of tuples that frame the event
  valid_times = []
  for ret in ret_list:
      (start_date,start_time) = json.dumps(ret_list[ret] ["start"]).split(' ')
      start_date = start_date.replace('"', '').strip()
      start_time = start_time.replace('"', '').strip()
      (end_date,end_time) = json.dumps(ret_list[ret] ["end"]).split(' ')
      end_date = end_date.replace('"', '').strip()
      end_time = end_time.replace('"', '').strip()
      valid_tuple = ((start_date,start_time),(end_date,end_time) )
      valid_times.append(valid_tuple)
  return (valid_times)


def authorize_user(an_event): # takes a dictionary, returns a list of user attributes tuples
  authorized_users = []
  unauthorized_users = []
  user_list = eb.list_event_attendees(an_event)
  people = user_list["attendees"]
  for ident in people:
    visitor = ident['attendee']
    try:
      name = json.dumps(visitor['first_name'])
      phone =json.dumps( visitor['cell_phone'])
      email = json.dumps(visitor['email'])
      vis = {"name":name, "phone":phone, "email":email}
      authorized_users.append(vis)
    except KeyError, e:
      unauthorized_users.append(json.dumps(visitor['email']))
      #print "there was an error found on ", visitor['email'], e  # debugging
  return ({"allowed" : authorized_users, "denied":unauthorized_users})
