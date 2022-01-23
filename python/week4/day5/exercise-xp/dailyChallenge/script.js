// 1. Create an array which value is the planets of the solar system.
let planets = [
  "mercury",
  "venus",
  "earth",
  "mars",
  "jupiter",
  "saturn",
  "uranus",
  "neptune",
];

// 2. For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// 4. Finally append each div to the <section> in the HTML (presented below).
let plaentColors = [
  "gray",
  "orange",
  "blue",
  "red",
  "brown",
  "yellow",
  "lightblue",
  "darkblue",
];
planets.forEach((element) => {
  let div = document.createElement("div");
  div.classList.add("planet");
  let section = document.getElementsByTagName("section");
  section[0].appendChild(div);
});

// 3.Each planet should have a different background color. (Hint: add a new class to each planet).

domPlanets = document.getElementsByClassName("planet");
console.log(domPlanets);
for (let i = 0; i < domPlanets.length; i++) {
  domPlanets[i].style.backgroundColor = plaentColors[i];
}
