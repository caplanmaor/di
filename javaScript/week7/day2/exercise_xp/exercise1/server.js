let http = require("http");

let handleRequest = (request, response) => {
  response.writeHead(200, {
    "Content-Type": "text/html",
  });
  response.write("<h2>Hi There!</h2><h1>test</h1><h4>end.</h4>");
  response.end();
};

http.createServer(handleRequest).listen(3000);
