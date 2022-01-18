let http = require("http");

const user = {
  firstname: "John",
  lastname: "Doe",
};

let handleRequest = (request, response) => {
  response.writeHead(200, {
    "Content-Type": "text/html",
  });
  response.write(JSON.stringify(user));
  response.end();
};

http.createServer(handleRequest).listen(8080);
