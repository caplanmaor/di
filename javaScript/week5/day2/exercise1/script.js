let xhr = new XMLHttpRequest();

function requestData() {
  xhr.open(
    "GET",
    "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
  );
  xhr.responseType = "json";
  xhr.send();
}

xhr.onload = function () {
  let gifs = xhr.response;
  console.log(gifs);
};

requestData();
