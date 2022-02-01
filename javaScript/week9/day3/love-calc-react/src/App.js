import logo from "./logo.svg";
import "./App.css";
import Fname from "./components/Fname";
import Sname from "./components/Sname";
import Calc from "./components/Calc";
import Result from "./components/Result";
import React from "react";
import { connect } from "react-redux";
import { findMatch } from "./redux/actions";

const App = () => {
  return (
    <div className="App">
      <Fname />
      <Sname />
      <Calc />
      <Result />
    </div>
  );
};

// const mapDispatchToProps = (dispatch) => {
//   return {
//     getAMatch: (data) => dispatch(findMatch(data)),
//   };
// };

// const mapStateToProps = (state) => {
//   return {
//     fname: state.fname,
//     sname: state.sname,
//   };
// };

export default App;
