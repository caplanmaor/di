// Create another component inside your Components folder, called Garage.js.

// Use an attribute to pass a size to the Garage component, <Garage size="small" />.

// Use the Garage component inside the Car component and pass the size ‘small’. The Garage component should render Who lives in my <size> Garage?

import React from "react";

class Garage extends React.Component {
  constructor() {
    super();
    this.state = {
      size: "",
    };
  }
  render() {
    return <h3>Who lives in my {this.props.size} Garage?</h3>;
  }
}
export default Garage;
