async function getInfo() {
  let randomInt = getRandomInt(49);

  function getRandomInt(max) {
    return Math.floor(Math.random() * max + 1);
  }
  let getJson = await fetch(`https://www.swapi.tech/api/people/${randomInt}`);
  let infoObject = await getJson.json();
  console.log(infoObject.result.properties);
  let info = infoObject.result.properties;
  document.getElementById("info").innerHTML =
    "name: " +
    info.name +
    "<br>" +
    " height: " +
    info.height +
    "<br>" +
    "hair color: " +
    info.hair_color;
}

document.getElementById("find").addEventListener("click", async () => {
  document.getElementById("loading").innerHTML = "lodaing";
  const nextContent = await getInfo();
  document.getElementById("loading").innerHTML = "";
});
