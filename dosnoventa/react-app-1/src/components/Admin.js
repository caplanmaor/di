import React from "react";
const axios = require("axios");

function Admin() {
  const [formData, setFormData] = React.useState({
    image: "",
    name: "",
    price: "",
  });

  const { image, name, price } = formData;

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const saveForm = () => {
    axios
      .post("http://localhost:3001/createBike", {
        data: formData,
      })
      .then(function (res) {
        console.log(res);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // console.dir(formData);
    saveForm();
  };

  let [select, setSelect] = React.useState("select a bike");

  const handleSelectChange = (e) => {
    setSelect(e.target.value);
  };

  return (
    <div>
      <h1>Admin Tools</h1>
      <h2>Remove Bikes</h2>
      <div>
        <select onChange={handleSelectChange}>
          <option value="a">a</option>
        </select>
        <br />
        <button>remove</button>
      </div>
      <h2>Add Bikes</h2>
      <form onSubmit={handleSubmit}>
        <h3>bike image</h3>
        <input
          type="text"
          name="image"
          value={image}
          onChange={handleInputChange}
        />
        <h3>bike name</h3>
        <input
          type="text"
          name="name"
          value={name}
          onChange={handleInputChange}
        />
        <h3>bike price</h3>
        <input
          type="text"
          name="price"
          value={price}
          onChange={handleInputChange}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Admin;
