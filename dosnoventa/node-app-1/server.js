const express = require("express");
const cors = require("cors");
var app = express();
app.use(cors());

var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: false }));

const { Pool, Client, Connection } = require("pg");
const { response } = require("express");
app.use(bodyParser.json());

app.listen(3001, () => {
  console.log("Server running on port 3001");
});

const credentials = {
  user: "postgres",
  host: "localhost",
  database: "dosnoventa",
  password: "postgres666",
  port: 5432,
};

async function getBikes() {
  const pool = new Pool(credentials);
  const res = await pool.query("SELECT * FROM bikes");
  await pool.end();

  return res.rows;
}

app.get("/bikes", (req, res) => {
  bikes = getBikes().then((result) => {
    res.json(result);
  });
});

async function createBike(bike) {
  let { image, name, price } = bike.data;
  // console.log(bike.data);
  const pool = new Pool(credentials);
  const res = await pool.query(
    `INSERT INTO bikes (img, name, price) VALUES ($1, $2, $3)`,
    [image, name, price],
    (err, results) => {
      console.log(err);
      console.log(results);
    }
  );
  await pool.end();
  // return res.rows;
}

app.post("/createBike", (req, res) => {
  createBike(req.body);
});

async function deleteBike(name) {
  bikeName = name.data;
  const pool = new Pool(credentials);
  const res = await pool.query(
    `DELETE FROM bikes WHERE name=$1 `,
    [bikeName],
    (err, results) => {
      console.log(err);
      console.log(results);
    }
  );
  await pool.end();
}

app.post("/deleteBike", (req, res) => {
  deleteBike(req.body);
});
