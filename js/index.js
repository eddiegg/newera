let server = require("./service");
let router = require("./router");
let requestHandlers=require("./requestHandlers");

let handle={};
handle["/"]=requestHandlers.start;
handle["/upload"]=requestHandlers.upload;
handle["/start"]=requestHandlers.start;

server.start(router.route,handle);