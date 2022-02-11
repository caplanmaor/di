const express = require("express");
const cors = require("cors");
var app = express();
app.use(cors());
app.listen(3001, () => {
  console.log("Server running on port 3001");
});

app.get("/bikes", (req, res) => {
  res.json([
    {
      id: 1,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_DET_Black_B_01_Flat-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®03 DET / JET BLACK BIKE",
      price: 2990,
    },
    {
      id: 2,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_LA_Green_B_01_Drop-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®02 LA / GREEN BIKE",
      price: 2890,
    },
    {
      id: 3,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_DET_Black_B_01_Flat-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®03 DET / JET BLACK BIKE",
      price: 2990,
    },
    {
      id: 4,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_LA_Green_B_01_Drop-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®02 LA / GREEN BIKE",
      price: 2890,
    },
    {
      id: 5,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_DET_Black_B_01_Flat-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®03 DET / JET BLACK BIKE",
      price: 2990,
    },
    {
      id: 6,
      img: "https://dosnoventabikes.com/wp-content/uploads/2020/10/DSNV_LA_Green_B_01_Drop-scaled-1960x1440.jpg",
      name: "DOSNOVENTA®02 LA / GREEN BIKE",
      price: 2890,
    },
  ]);
});
