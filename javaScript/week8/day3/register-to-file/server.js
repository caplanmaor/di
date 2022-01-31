const exp = require("express");
const cors = require("cors");
const env = require("dotenv");
const fs = require("fs");

const app = exp();
// app.use(exp.urlencoded());
app.use(exp.json());
app.use(cors());

env.config();

app.listen(process.env.PORT, () => {
  console.log(`PORT=${process.env.PORT}`);
});

const usersData = fs.readFileSync("./users.json");
const users = JSON.parse(usersData);
console.log(users);

app.post("/register", (req, res) => {
  console.log(req.body);
  if (userExists(req.body.username)) {
    res.json({ message: "Not Ok" });
  } else {
    users.push(req.body);
    fs.writeFile("./users.json", JSON.stringify(users), (err) => {
      if (err) {
        console.log(err);
      }
      res.json({ message: "OK" });
    });
  }
});

const userExists = (username) => {
  return users.find((item) => item.username == username);
};
