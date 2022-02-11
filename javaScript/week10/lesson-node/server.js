import express from "express";
import dotenv from "dotenv";
import cors from "cors";

dotenv.config();

const app = express();

const auth = (req, res, next) => {
  console.log("test");
  if (auth == false) res.json({ msg: "login again" });
  next();
};

app.use(cors());
app.use(express.json());
app.use(auth);

app.get("/login", (req, res) => {
  res.json({ msg: "hello" });
});

app.get("/register", (req, res) => {
  console.log(register);
});

app.listen(process.env.PORT, () => {
  console.log(`listen to port ${process.env.PORT}`);
});
