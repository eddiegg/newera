let http = require("http");

http.createServer(function(request,response){
    response.writeHead(200,{"Content-Type":"text/plain"});
    response.write("hi,eddie");
    response.end();
}).listen(9999);