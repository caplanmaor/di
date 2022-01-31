import React from "react";
import "./App.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
    };
  }

  addOne = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div className="App">
        <button onClick={this.addOne}> Add One </button>
        {this.state.count}
      </div>
    );
  }
}

export default App;
