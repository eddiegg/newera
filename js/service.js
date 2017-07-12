let http = require("http");
let url = require("url");

function start(route) {
    function onRequest(request, response) {
        let pathname = url.parse(request.url).pathname;
        console.log("Request for " + pathname + " received.");

        route(pathname);

        response.writeHead(200, { "Content-Type": "text/plain" });
        response.write("hi,eddie");
        response.end();
    }
    http.createServer(onRequest).listen(9999);
    console.log("server started");
}

exports.start = start;