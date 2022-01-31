import logo from "./logo.svg";
import "./App.css";
import LoadQuote from "./components/LoadQuote";
import quotes from "./components/QuoteDatabase";
import React from "react";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      quote: quotes[10],
    };
  }
  getRandomNumber = () => {
    return Math.floor(Math.random() * quotes.length - 1);
  };
  handleClick = () => {
    const num = this.getRandomNumber();
    this.setState({ quote: quotes[num] });
  };

  render() {
    return (
      <div className="App">
        <LoadQuote />
      </div>
    );
  }
}

export default App;
