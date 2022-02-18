const express = require("express");
const { Pool, Client } = require("pg");
const cors = require("cors");
const { response } = require("express");
var app = express();
app.use(cors());
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
