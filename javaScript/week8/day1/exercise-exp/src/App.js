import logo from "./logo.svg";
import "./App.css";
import React from "react";
import UserFavoriteAnimals from "./UserFavoriteColors";
import Exercise4 from "./Exercise4";

// exercise 1

// class Element extends React.Component {
//   render() {
//     return React.createElement("h1", null, "i dont use jsx");
//   }
// }

// function App() {
//   return (
//     <div className="App">
//       <Element />
//     </div>
//   );
// }

// export default App;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// exercise 2

// 1 display hello world
// 2 Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page.
// const myelement = <h1>i love JSX!</h1>;

// 3 Create a constant variable named sum, which value is 5 + 5. Render on the page, the following sentence "React is <sum> times better with JSX"
// const sum = 5 + 5;

// function App() {
//   return (
//     <div>
//       <h2> Hello World!</h2>
//       {myelement}
//       <h3>react is {sum} times better with jsx</h3>
//     </div>
//   );
// }

// export default App;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// exercise 3
const user = {
  first_name: "Bob",
  last_name: "Dylan",
  fav_animals: ["Horse", "Turtle", "Elephant", "Monkey"],
};

let array = user.fav_animals;

function App() {
  return (
    <div>
      <h3>{user.first_name}</h3>
      <h3>{user.last_name}</h3>
      <UserFavoriteAnimals array={array} />
      <Exercise4 />
    </div>
  );
}

// In a separate Javascript file, create a new Component called UserFavoriteColors. Use props to pass the fav_animals array to the UserFavoriteColors component.

export default App;

///////////////////////////
