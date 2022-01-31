import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Card from "./components/Card";
class App extends React.Component {
  constructor() {
    super();
    this.state = {
      arr: [],
    };
  }
  componentDidMount() {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        this.setState({ arr: data });
      });
  }
  render() {
    const { arr } = this.state;
    return (
      <>
        {arr.map((item, i) => {
          return <Card user={item} />;
        })}
      </>
    );
  }
}

export default App;
