let server = require("./service");
let router = require("./router");
server.start(router.route);