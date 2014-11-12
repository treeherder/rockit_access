from secret import *
import json

r = eb.user_list_events()

def touch_events():  #returns a dictionary of live events
  ret_list = {}
  for x in xrange(len(r['events'])):  #iterate over the events
    ret={}
    if (r['events'][x]['event']['status'] == "Live" ):
      ret['id']=r['events'][x]['event']['id']
      ret['title'] = r['events'][x]['event']['title']
      ret['status'] = r['events'][x]['event']['status']
      ret['start'] = r['events'][x]['event']['start_date']
      ret['end'] = r['events'][x]['event']['end_date']
      ret_list[ret['id']] = (ret)
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


def authorize_user(ret_list): # takes a dictionary 
  authorized_users = []
  for a_event in ret_list:
    event = eb.list_event_attendees({'id':ret_list[a_event]['id']})
    people = event["attendees"]
    for ident in people:
      visitor = ident['attendee']
      try:
        name = visitor['first_name']
        phone = visitor['cell_phone']
        email = visitor['email'] 
        vis = (name, phone, email)
        authorized_users.append(vis)
      except KeyError, e:
        print "there was an error found on ", visitor['email'], e
  print (authorized_users)
  return (authorized_users) 