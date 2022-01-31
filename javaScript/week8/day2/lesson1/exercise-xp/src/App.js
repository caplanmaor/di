import logo from "./logo.svg";
import React from "react";
import "./App.css";
import RenderCarInfo from "./components/Car";
import { render } from "@testing-library/react";
import Events from "./components/Events";

// 1. In App.js create an object, In your React app create a new folder in the src path, name it Components. It should contain a Class Component named Car.js.
const carinfo = { name: "Ford", model: "Mustang", color: "red" };

const handleKeyPress = (props) => {
  console.log("handleKeyPress");
};
// In the render() method, create a button that when clicked on, calls the clickMe function.
function App() {
  return (
    <div>
      <RenderCarInfo model={carinfo.model} color={carinfo.color} />
      <button onClick={Events().clickMe}>click me</button>
      <br />
      <input type="text" onKeyPress={handleKeyPress()} />
    </div>
  );
}

export default App;
