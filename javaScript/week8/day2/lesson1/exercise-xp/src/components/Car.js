import React from "react";
import Garage from "./Garage";
// In the Car.js component render a header with the carInfo model, for example This car is <model>.
// Create a constructor function in the Car component, and add a color property in the state.
// Display the color property in the render() method, for example This car is <color> <model>.
class RenderCarInfo extends React.Component {
  constructor() {
    super();
    this.state = {
      color: "",
      mode: "",
    };
  }
  render() {
    return (
      <div>
        <h2>
          the car color is {this.props.color} and the model is{" "}
          {this.props.model}
        </h2>
        <Garage size={"small"} />
      </div>
    );
  }
}
export default RenderCarInfo;
