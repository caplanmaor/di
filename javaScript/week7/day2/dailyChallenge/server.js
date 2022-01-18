const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();
const port = process.env.PORT || 8080;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/aboutMe/:hobby", function (req, res) {
  if (isNaN(req.params.hobby)) {
    res.send(req.params.hobby);
  } else {
    res.send("404");
  }
});

app.get("/pic", function (req, res) {
  res.sendFile(path.join(__dirname, "./public/index.html"));
});

app.get("/form", (req, res) => {
  res.sendFile(path.join(__dirname, "./public/form.html"));
});

app.post("/formData", (req, res) => {
  console.log(req.body);
  res.send(
    `the email is: ${req.body.email} and the message is: ${req.body.message}`
  );
});

app.listen(port);
console.log("Server started at http://localhost:" + port);
