// Create a new Class component named Events.
function Events(props) {
  // Create an arrow function called clickMe. It should alert the string ‘I was clicked’.
  const clickMe = () => {
    return alert("i was clicked");
  };
  return { clickMe };
}

export default Events;
