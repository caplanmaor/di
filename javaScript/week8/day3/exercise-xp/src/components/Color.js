import React from "react";

class Color extends React.Component {
  state = {
    color: "red",
  };

  //   shouldComponentUpdate() {
  //     return false;
  //   }

  componentDidMount() {
    setInterval(() => {
      this.setState({
        color: "blue",
      });
    }, 5000);
  }

  render() {
    return <h2>my fav color is {this.state.color}</h2>;
  }
}

export default Color;
