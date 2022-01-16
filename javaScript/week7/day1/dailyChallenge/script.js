import { largeNumber } from "./main.js";
import { dateAndTime } from "./main.js";
import * as http from "http";

const b = 5;
console.log(largeNumber + b);

http
  .createServer(function (req, res) {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.write(
      b + largeNumber + "<br>" + " Hello front!" + "<br>" + dateAndTime()
    );
    res.end();
  })
  .listen(3000);
console.log("listening");
