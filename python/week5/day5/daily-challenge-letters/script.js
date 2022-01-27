let input = document.getElementById("text-input");

input.addEventListener("keydown", logKey);

function logKey(e) {
  e.preventDefault();
  if (e.key.match(regex)) {
    input.value += e.key;
  }
}

regex = /^[A-Za-z.\s_-]+$/;
