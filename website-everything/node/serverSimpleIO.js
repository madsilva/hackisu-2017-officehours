var mysql = require("mysql");
var http = require("http");

var connection = mysql.createConnection({
  host: 'phly.c7jx0v6pormd.us-east-1.rds.amazonaws.com',
  user: 'phly',
  password: 'phlyisthebest',
  port: '3306',
  database : 'phly'
});

connection.connect(function(err) {
    if (err) {
        console.error('error connecting: ' + err.stack);
        return;
    }
    console.log("connected");
});


var server = http.createServer((req, res)=>{
    res.writeHead(200, {'Content-Type': 'text/plain'});

    var userInput = (req.url).split('?')[1];

    if(userInput == 'get') {
        res.write("callback(\"" + currentlyServing() + "\");");
        res.end();
    } else if(userInput.split('=')[0] === 'insert') {
        res.write("insertStatus(\"" + insertStatus(userInput.split('=')[1]) + "\");");
        res.end();
    }

}).listen(3000);


var currentlyServing = function() {
    var data;
    console.log("serve");
    return "serving you.";
}

var insertStatus = function(data) {
    console.log("insert");
    return data;
}
