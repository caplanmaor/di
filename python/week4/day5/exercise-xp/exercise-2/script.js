//Exercise 2 : Users
// 1.In the HTML above change the name “Pete” to “Richard”.
document
  .getElementsByTagName("ul")[0]
  .getElementsByTagName("li")[1].textContent = "richard";

// 2. Change each first name of the two <ul>'s to your name.
for (let i = 0; i < 2; i++) {
  document
    .getElementsByTagName("ul")
    [i].getElementsByTagName("li")[0].textContent = "maor";
}

// 3. At the end of each <ul> add a <li> that says “Hey students”
uls = document.getElementsByTagName("ul");
for (let i = 0; i < uls.length; i++) {
  let heyLi = document.createElement("li");
  let heyTextNode = document.createTextNode("hey students");
  heyLi.appendChild(heyTextNode);
  uls[i].appendChild(heyLi);
}

// 4. delete sarah
let lis = uls[1].getElementsByTagName("li");
for (let i = 0; i < lis.length; i++) {
  if (lis[i].textContent == "Sarah") {
    lis[i].remove();
  }
}
