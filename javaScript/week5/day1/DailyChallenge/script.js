let form = document.getElementById("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  let urlSearchParamsObj = new URLSearchParams(window.location.search);
  let [key, value] = urlSearchParamsObj.entries();
  document.getElementById("results").textContent = key + " : " + value;
});
