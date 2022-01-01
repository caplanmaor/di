const users = { user1: 18273, user2: 92833, user3: 90315 };

let usersArray = Object.entries(users);
console.log(usersArray);

for (let user of usersArray) {
  user[1] *= 2;
}
