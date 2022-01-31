import React from "react";
import "./App.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      languages: [
        { name: "Php", votes: 0 },
        { name: "Python", votes: 0 },
        { name: "JavaSript", votes: 0 },
        { name: "Java", votes: 0 },
      ],
    };
  }

handleClick = (val) => {
  this.state.languages[val].votes++
  let newLanguages = [...this.state.languages]
  this.setState({languages: newLanguages});
}

  render() {
    return (
      <div>
        {
          this.state={languages.map((item,i) => {
            return(
              "a"
            )
          })
        }}
      </div>
    )}

      }

export default App;
