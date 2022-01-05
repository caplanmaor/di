let xhr = new XMLHttpRequest();
let searchButton = document.getElementById("searchbtn");
let searchValue = "";
let gif = "";
let catalog = document.getElementById("catalog");

searchButton.addEventListener("click", (e) => {
  let randomNum = Math.floor(Math.random() * 100) + 1;
  e.preventDefault();
  searchValue = document.getElementById("searchbox").value;
  xhr.open(
    "GET",
    `https://api.giphy.com/v1/gifs/search?q=${searchValue}&rating=g&limit=1&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My&offset=${randomNum}`
  );
  xhr.responseType = "json";
  xhr.send();
});

xhr.onload = function () {
  gif = xhr.response.data[0].images.downsized.url;
  createGif();
};

function createGif() {
  let gifCard = document.createElement("div");
  let img = document.createElement("img");
  img.src = gif;
  img.classList.add("img");
  gifCard.appendChild(img);
  gifCard.classList.add("gifcard");
  let removeBtn = document.createElement("button");
  removeBtn.classList.add("removebtn");
  removeBtn.addEventListener("click", (e) => {
    e.target.parentElement.style.display = "none";
  });
  removeBtn.textContent = "remove";
  gifCard.appendChild(removeBtn);
  catalog.appendChild(gifCard);
}

//remove all
document.getElementById("removeall").addEventListener("click", (e) => {
  e.preventDefault();
  cards = document.getElementsByClassName("gifcard");
  for (let card of cards) {
    card.style.display = "none";
  }
});
