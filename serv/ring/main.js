var express = require('express'),
    bodyParser = require('body-parser');
var moment = require('moment');

var app = express();
app.use(bodyParser.urlencoded({
    extended: false
}));

app.post('/doorbell', function(req, res) {
    // in this function, we need to route the visitor based on their post data and the relevant
    //feedback from our backend
    //we can generate on-the-fly xml  or plain text components to reply to messages intelligently
    //first we get the message data

    var now = moment().format('MMMM Do YYYY, h:mm:ss a');


    var from = req.body.From,
        body = req.body.Body;

    console.log(now + "    " + from + "      " + body);
    //res.send(200);
var child_process = require('child_process');
child_process.exec('python /root/rockit_access/r_a.py -u '+ from +' -M -m "'+ body +'"', function (err, stdout, stderr){
    if (err) {
        console.log("child processes failed with error code: " +
            err.code);
    }
    console.log(stdout);
});


});





require('http').createServer(app).listen(80, function(){
    console.log("ready");});
