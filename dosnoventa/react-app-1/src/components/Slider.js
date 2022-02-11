import React, { useEffect, useState } from "react";
import axios from "axios";

function Slider() {
  const [responseBikes, setResponseBikes] = useState(null);
  // Define the function that fetches the data from API
  const fetchData = async () => {
    const { data } = await axios.get("http://localhost:3001/bikes");
    setResponseBikes(data);
  };

  // Trigger the fetchData after the initial render by using the useEffect hook
  useEffect(() => {
    fetchData();
  }, []);
  console.log(responseBikes);

  let bikes = [
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
  ];
  return (
    <div className="slider">
      {bikes.map((bike) => (
        <div className="bike" key={bike.id}>
          <img className="bike-img" src={bike.img}></img>
          <h3 className="bike-name">{bike.name}</h3>
          <h2 className="bike-price">{bike.price}</h2>
        </div>
      ))}
    </div>
  );
}

export default Slider;
