import logo from "./logo.svg";
import "./App.css";
import React from "react";
import ErrorBoundary from "./components/ErrorBoundary";
import BuggyCounter from "./components/BuggyCounter";
import Color from "./components/Color";

function App() {
  return (
    <div className="App">
      <h2>wlecome to the crashing app part 1</h2>
      <ErrorBoundary>
        <BuggyCounter />
        <BuggyCounter />
      </ErrorBoundary>
      <h2>wlecome to the crashing app part 2</h2>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <h2>wlecome to the crashing app part 3</h2>
      <BuggyCounter />
      <Color />
    </div>
  );
}

export default App;
