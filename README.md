rockit_access
=============

a bare-bones access system API for a san francisco based co-working and hacking space



Classes and methods from engine:
------------------
Txtr:
- called with an argument to initialize the database and collection (in this case db='test', col = 'rockit')  
- send_text("message", "receiver"):
  -sends message to receiver 
- get text():
  - prints  all messages sent to the number hardcoded into the library

Calendar
- provides query functions to scheduling data
- list_timeslots():
  - returns a list of profiles who are expected at the event, if there is currently an event


####Dependencies
--------
#####packages:
 -eventbrite
 -twilio

#####files:
-secret.py


TODO:
-----
1. []make everything work of off secret auth info file
2. []make engine methods return instead of simply print