from secret import *
import json

r = eb.user_list_events()

def touch_events():  #gets live events 
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

def authorize_schedule(ret_list):  #returns a list of tuples that frame the event 
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


def authorize_user():

  for x in xrange(len(ret_list)):
    person = eb.list_event_attendees({'id':ret_list[x]['id']})
    print person

for x in authorize_schedule(touch_events()):
  print x
