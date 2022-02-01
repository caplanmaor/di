import logo from "./logo.svg";
import "./App.css";
import React from "react";
import MovieList from "./components/MovieList";
import MovieDetail from "./components/MovieDetail";

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      movies: [
        {
          title: "Spider-Man: Homecoming",
          releaseDate: "05-07-2017",
          rating: 7.4,
        },
        { title: "Aquaman", releaseDate: "12-07-2018", rating: 7 },
        { title: "Black Panther", releaseDate: "02-13-2018", rating: 7.4 },
        {
          title: "Avengers: Infinity War",
          releaseDate: "04-25-2018",
          rating: 8.3,
        },
        {
          title: "Guardians of the Galaxy",
          releaseDate: "07-30-2014",
          rating: 7.9,
        },
      ],
      detail: null,
    };
  }

  selectMovie = (param) => {
    this.setState({ detail: param });
  };

  render() {
    return (
      <div className="App">
        <MovieList movies={this.state.movies} selectMovie={this.selectMovie} />
        <MovieDetail detail={this.state.detail} />
      </div>
    );
  }
}

export default App;
