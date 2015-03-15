function urlQueryGetter(url){
        //array to store params
        var qParam = new Array();
        //function to get param
        this.getParam = function(x){
              return qParam[x];

}

        //parse url
        query = url.substring(url.indexOf('?')+1);
        query_items = query.split('&');
        for(i=0; i<query_items.length;i++){
                  s = query_items[i].split('=');
                  qParam[s[0]] = s[1];

}
};

var http = require('http');




var postHTML =
  '<html><head><title>Rockit Access</title></head>' +
  '<body>'+
  '</body></html>';

http.createServer(function (req, res) {
  var body = "";
  req.on('data', function (chunk) {
    body += chunk;
  var getter = new urlQueryGetter(body);
  from = (getter.getParam('From'));
  msg = (getter.getParam('Body'));
  msg = msg.replace(/[+]/g, ' ');  // strip the formatting for word split
  msg = decodeURIComponent(msg);
  });

  req.on('end', function() {
    console.log('POSTed: ' + msg + 'from' + from);
     res.writeHead(200);
    res.end(postHTML);


  });
}).listen(8080);
