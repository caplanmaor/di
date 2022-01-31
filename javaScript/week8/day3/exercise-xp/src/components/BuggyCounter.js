import React from "react";

class BuggyCounter extends React.Component {
  state = {
    counter: 0,
  };

  handleClick = () => {
    this.setState({
      counter: this.state.counter + 1,
    });
  };

  render() {
    if (this.state.counter === 5) {
      // Simulate an error!
      throw new Error("dont go above 5");
    }
    return (
      <div>
        {/* <h4>click to raise the number</h4> */}
        <h1 onClick={this.handleClick}>{this.state.counter}</h1>
      </div>
    );
  }
}

export default BuggyCounter;
