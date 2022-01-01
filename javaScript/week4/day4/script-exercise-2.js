function getMoreDetails({ Name, House, Friend: { FriendName, Age } }) {
  console.log(Name, House, FriendName, Age);
}

getMoreDetails({
  Name: "Hermione Granger",
  House: "Gryfindor",
  Friend: {
    FriendName: "Harry Potter",
    Age: 20,
  },
});
