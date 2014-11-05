from secret import *
import json

r = eb.user_list_events()
ret_list ={}

def touch_events():
  for x in xrange(len(r['events'])):  #iterate over the events
    ret={}
    if (r['events'][x]['event']['status'] == "Live" ):
      ret['id']=r['events'][x]['event']['id']
      ret['title'] = r['events'][x]['event']['title']
      ret['status'] = r['events'][x]['event']['status']
      ret['start'] = r['events'][x]['event']['start_date']
      ret['end'] = r['events'][x]['event']['end_date']
      ret_list[ret['id']] = (ret)


def authorize_schedule():
  valid_times = ()
  for ret in ret_list:
      #print ret_list[ret] ["start"],
      #print ret_list[ret] ["end"]
      (start_date,start_time) = json.dumps(ret_list[ret] ["start"]).split(' ')
      start_date = start_date.replace('"', '').strip()
      start_time = start_time.replace('"', '').strip()
      print( (start_date,start_time) )

      (end_date,end_time) = json.dumps(ret_list[ret] ["end"]).split(' ')
      end_date = end_date.replace('"', '').strip()
      end_time = end_time.replace('"', '').strip()
      print( (end_date,end_time) )



def authorize_user():
  for x in xrange(len(ret_list)):
    person = eb.list_event_attendees({'id':ret_list[x]['id']})
    print person

touch_events()
authorize_schedule()
