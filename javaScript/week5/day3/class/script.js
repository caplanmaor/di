let getRandomWordUrl = "http://random-word-api.herokuapp.com/word?number=1";
let randomWord = "";
function requestWord() {
  fetch(getRandomWordUrl)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      randomWord = data[0];
      console.log(randomWord);
    });
}

requestWord();

let getGifUrl = `https://api.giphy.com/v1/gifs/random?tag=${randomWord}&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`;
let randomGifUrl = "";

function requestGif() {
  fetch(getGifUrl)
    .then((response) => {
      if (response.status == 200) {
        return response.json();
      } else {
        throw new Error("not 200");
      }
    })
    .then((data) => {
      randomGifUrl = data.data.images.downsized.url;
      appendGif(randomGifUrl);
    })
    .catch((error) => {
      console.log("catch", error);
      //404 gif
      randomGifUrl =
        "https://media4.giphy.com/media/5QJd1IC6yBLumMhmtu/giphy.gif?cid=830e7a840efcc55054aea9eb8583404947ba627304652b60&rid=giphy.gif&ct=g";
      appendGif(randomGifUrl);
    });
  return randomGifUrl;
}

randomGifUrl = requestGif();
// appendGif(gif);

// console.log(randomGifUrl);

function appendGif(gif) {
  let img = document.createElement("img");
  img.src = randomGifUrl;
  document.getElementById("gifHolder").appendChild(img);
}
