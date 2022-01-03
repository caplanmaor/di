let xhr = new XMLHttpRequest();

function requestData() {
  xhr.open("GET", "https://jsonplaceholder.typicode.com/users");
  xhr.responseType = "json";
  xhr.send();
}

xhr.onload = function () {
  let people = xhr.response;
  for (let i = 0; i < 3; i++) {
    console.log(people[i].name);
    console.log(people[i].email);
    console.log(people[i].address.city);
    console.log("---------------");
  }
};
requestData();
