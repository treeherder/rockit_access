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
- should find  IS THERE AN EVENT RIGHT NOW
- should find  WHO IS EXPECTED TO ATTEND

- list_timeslots():
  - a list of tuples of that are (start , end) tuples of (date, time) tuples
    - [ ( (start date,  start time), (end date, end time) ) ,( (start date,  start time), (end date, end time) ), etc. ...]



####Dependencies
------
#####packages:
 - eventbrite
   * `pip install eventbrite`
 - pycurl
   * `pip install pycurl`
 - twilio
   * `pip install twilio`



#####files for internal API:
-secret.py

TODO:
-----
1. [X] make everything work of off secret auth info file
2. [X] make engine methods return instead of simply print
3. [X] handle real-time requests
4. [X] make example scripts
5. [] make timechecking failsafe - spawn second instance under "Live" to check for right_now() ?