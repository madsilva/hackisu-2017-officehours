var mysql = require("mysql");

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

    var functionCall = userInput.split('/')[0];
    if(userInput.split('/')[1]) var data = userInput.split('/')[1];


    if(functionCall === 'get') {
        res.write("callback(" + currentlyServing() + ")");
        res.end();
    }

    else if(functionCall === 'insert') {
        res.write("callback(" + insertStatus() + ")");
        res.end();
    }
}).listen(3000);


var currentlyServing = function() {
    var data;
    return "serving you.";
}

var insertStatus = function() {
    return "insert";
}
