// 1. Add a “light blue” background color and some padding to the <div>.
document.getElementsByTagName("div")[0].style.backgroundColor = "lightblue";
document.getElementsByTagName("div")[0].style.padding = "50px";

// 2. Do not display the first name (John) in the list.
document.getElementsByTagName("ul")[0].children[0].style.display = "none";

// 3. Add a border to the second name (Pete).
document.getElementsByTagName("ul")[0].children[1].style.border =
  "1px solid black";

// 4. Change the font size of the whole body.
document.getElementsByTagName("body")[0].style.fontSize = "25px";
