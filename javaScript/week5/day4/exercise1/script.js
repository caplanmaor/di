// fetch("https://swapi.dev/api/starships/9/")
//   .then((response) => response.json())
//   .then(console.log);

async function getData() {
  let response = await fetch("https://swapi.dev/api/starships/9/");
  let data = await response.json();
  console.log(data);
}
getData();
