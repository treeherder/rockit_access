rockit_access
=============

a bare-bones access system API for a san francisco bsaed co-working and hacking space



Classes and methods:
------------------
Txtr:
  - called with an argument to initialize the database and collection (in this case db='test', col = 'rockit')
  
  - send_text("message", "receiver"):
      --sends message to receiver 
  
  - get text():
      -- prints  all messages sent to the number hardcoded into the library