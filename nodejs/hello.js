#!/usr/bin/env nodejs
var http = require('http');

http.createServer(function (req, res) {
	  res.writeHead(200, {'Content-Type': 'text/plain'});
	  res.end('Hello World\n');
}).listen(1234, '172.17.111.26');
console.log('Server running at http://localhost:8080/');