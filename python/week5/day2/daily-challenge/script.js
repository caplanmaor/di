let button = document.getElementById("lib-button");
// let story = document.getElementById("story");

button.addEventListener("click", (e) => {
  e.preventDefault();
  story();
});

function story() {
  let noun = document.getElementById("noun").value;
  let adjective = document.getElementById("adjective").value;
  let pname = document.getElementById("person").value;
  let verb = document.getElementById("verb").value;
  let place = document.getElementById("place").value;
  let allValues = [noun, adjective, pname, verb, place];
  for (let element of allValues) {
    if (element == "") {
      window.alert("cant use empty values");
      return;
    } else {
      document.getElementById(
        "story"
      ).innerText = `when ${pname} tried to ${verb} a ${noun} in ${place} he failed because he was too ${adjective}`;
    }
  }
}
