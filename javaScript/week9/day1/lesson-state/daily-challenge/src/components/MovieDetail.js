const MovieDetail = (props) => {
  const { detail } = props;
  if (!detail) {
    return (
      <div>
        <h2>Movie Detail</h2>
        <p>choose a movie</p>
      </div>
    );
  } else {
    return (
      <div>
        <h2>Movie Detail</h2>
        <p>title: {detail.title}</p>
        <p>release: {detail.releaseDate}</p>
        <p>rating: {detail.rating}</p>
      </div>
    );
  }
};
export default MovieDetail;
