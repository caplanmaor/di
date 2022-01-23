import { render } from "@testing-library/react";
import React from "react";

const user = {
  first_name: "Bob",
  last_name: "Dylan",
  fav_animals: ["Horse", "Turtle", "Elephant", "Monkey"],
};

// 2.In a separate Javascript file, create a new Component called UserFavoriteColors. Use props to pass the fav_animals array to the UserFavoriteColors component.
// function UserFavoriteAnimals(props) {
//   return <h1>{props.array}</h1>;
// }

// 3. In the UserFavoriteColors component, use the map function to create a new array of <li>‘s.
function UserFavoriteAnimals(props) {
  return (
    <div>
      <ul>
        {props.array.map((e, i) => {
          return <li key={i}> {e} </li>;
        })}
      </ul>
    </div>
  );
}

export default UserFavoriteAnimals;
