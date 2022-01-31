import React from "react";
import "./App.css";
import cards from ".//components/superheroes.json";

localStorage.setItem("highscore", 0);

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      superheroes: cards.superheroes,
      score: 0,
      id: [],
    };
  }

  reset = () => {
    window.location.reload(false);
    localStorage.setItem("highscore", 0);
  };

  click = (e) => {
    let id = e.target.id;
    this.setState({ id: [...this.state.id, id] });
    this.setState({
      superheroes: this.state.superheroes.sort(() => 0.5 - Math.random()),
    });
    if (this.state.id.includes(e.target.id)) {
      this.setState({ score: 0 });
      this.setState({ id: [] });
    } else {
      this.setState({ score: this.state.score + 1 });
      if (this.state.score + 1 > localStorage.getItem("highscore")) {
        localStorage.setItem("highscore", this.state.score + 1);
      }
    }
  };

  render() {
    return (
      <div className="App">
        <div className="text">
          <div>high score {localStorage.getItem("highscore")}</div>
          <div>Score {this.state.score}</div>
          <button className="reset" onClick={this.reset}>
            reset high score
          </button>
        </div>
        <div className="card-holder">
          {this.state.superheroes.map((element, i) => {
            return (
              <div
                className="card"
                onClick={this.click}
                id={element.id}
                key={i}
                className="card"
              >
                <img id={element.id} src={element.image}></img>
                <h3>
                  <b>Name:</b> {element.name}
                </h3>
                <h4>
                  <b>Job:</b> {element.occupation}
                </h4>
              </div>
            );
          })}
        </div>
      </div>
    );
  }
}

export default App;
