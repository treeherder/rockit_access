from secret include *

 r = eb.user_list_events()


ret_list = []
for x in xrange(len(r['events'])):  #iterate over the events
  ret={}
  if (r['events'][x]['event']['status'] == "Live" ):  
    ret['id']=r['events'][x]['event']['id']
    ret['title'] = r['events'][x]['event']['title']
    ret['status'] = r['events'][x]['event']['status']
    ret['start'] = r['events'][x]['event']['start_date']
    ret['end'] = r['events'][x]['event']['end_date']
    ret_list.append(ret)
    

