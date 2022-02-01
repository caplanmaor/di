export const setNames = (name, value) => {
  return {
    type: name,
    payload: value,
  };
};

export const findMatch = (sname, fname) => (dispatch) => {
  fetch(
    `https://love-calculator.p.rapidapi.com/getPercentage?sname=${sname}&fname=${fname}`,
    {
      method: "GET",
      headers: {
        "x-rapidapi-host": "love-calculator.p.rapidapi.com",
        "x-rapidapi-key": "07602e5978msh111462e8148c894p1c8480jsnb70aa5928ba7",
      },
    }
  )
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      // this.setState({ results: data });
      dispatch({ type: "FIND_MATCH", payload: data });
    })
    .catch((err) => {
      console.error(err);
    });
};
