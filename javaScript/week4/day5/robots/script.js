const robots = [
  {
    id: 1,
    name: "Leanne Graham",
    username: "Bret",
    email: "Sincere@april.biz",
    image: "https://robohash.org/1?200x200",
  },
  {
    id: 2,
    name: "Ervin Howell",
    username: "Antonette",
    email: "Shanna@melissa.tv",
    image: "https://robohash.org/2?200x200",
  },
  {
    id: 3,
    name: "Clementine Bauch",
    username: "Samantha",
    email: "Nathan@yesenia.net",
    image: "https://robohash.org/3?200x200",
  },
  {
    id: 4,
    name: "Patricia Lebsack",
    username: "Karianne",
    email: "Julianne.OConner@kory.org",
    image: "https://robohash.org/4?200x200",
  },
  {
    id: 5,
    name: "Chelsey Dietrich",
    username: "Kamren",
    email: "Lucio_Hettinger@annie.ca",
    image: "https://robohash.org/5?200x200",
  },
  {
    id: 6,
    name: "Mrs. Dennis Schulist",
    username: "Leopoldo_Corkery",
    email: "Karley_Dach@jasper.info",
    image: "https://robohash.org/6?200x200",
  },
  {
    id: 7,
    name: "Kurtis Weissnat",
    username: "Elwyn.Skiles",
    email: "Telly.Hoeger@billy.biz",
    image: "https://robohash.org/7?200x200",
  },
  {
    id: 8,
    name: "Nicholas Runolfsdottir V",
    username: "Maxime_Nienow",
    email: "Sherwood@rosamond.me",
    image: "https://robohash.org/8?200x200",
  },
  {
    id: 9,
    name: "Glenna Reichert",
    username: "Delphine",
    email: "Chaim_McDermott@dana.io",
    image: "https://robohash.org/9?200x200",
  },
  {
    id: 10,
    name: "Clementina DuBuque",
    username: "Moriah.Stanton",
    email: "Rey.Padberg@karina.biz",
    image: "https://robohash.org/10?200x200",
  },
];

createRobots();
search();

function createRobots() {
  let catalog = document.getElementById("catalog");
  for (let robot of robots) {
    //robot card
    let robotCard = document.createElement("div");
    robotCard.classList.add("robotcard");
    //robot name
    let robotName = document.createElement("p");
    robotName.innerText = robot.name;
    robotCard.appendChild(robotName);
    //robot image
    let robotImage = document.createElement("img");
    robotImage.src = robot.image;
    robotCard.appendChild(robotImage);
    //append card to catalog
    catalog.appendChild(robotCard);
  }
}

function search() {
  document.getElementById("searchbtn").addEventListener("click", function (e) {
    e.preventDefault();
    let input = document.getElementById("searchbox");
    let searchFilter = input.value.toUpperCase();
    let searchRobots = document.getElementsByClassName("robotcard");
    for (let robot of searchRobots) {
      let robotName = robot.firstChild;
      let robotNameText = robotName.textContent;
      robotNameText.toUpperCase().indexOf(searchFilter) > -1
        ? (robot.style.display = "flex")
        : (robot.style.display = "none");
    }
  });
}
