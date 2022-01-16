export { largeNumber };
export { dateAndTime };
const largeNumber = 356;

function dateAndTime() {
  let date = new Date(Date.now());
  let formattedDate = date.toLocaleString();
  return formattedDate;
}
