import React from "react";
import "./Exercise4.css";

function Exercise4() {
  const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial",
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        gap: "20px",
      }}
    >
      {/* <h1 style={{ color: "red", backgroundColor: "lightblue" }}>
        This is a Header
      </h1> */}
      <h1 style={style_header}>this is a header</h1>
      <p className="para">this is a paragrpah</p>
      <a href="#">this is a link</a>
      <form>
        <input placeholder="type here"></input>
        <button>test</button>
      </form>
      <img src="https://i.pinimg.com/favicons/1f4dc41bdea9a7949350559750cd5f7fa274fdb3ede6220fbedca3a4.ico?67ff863029654c19bad44e9b0b2fe520"></img>
      <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
      </ul>
    </div>
  );
}

export default Exercise4;
