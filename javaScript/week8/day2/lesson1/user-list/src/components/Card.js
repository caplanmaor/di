const Card = (props) => {
  // const {user} = props;
  const { id, email, name } = props.user;
  return (
    <div>
      <div>
        <img src={`https://robohash.org/${id}?size=150x150`} />
      </div>
      <div className="tc grow bg-light-green br3 pa3 ma3 dib shadow-5">
        <h4>{name}</h4>
        <p>{email}</p>
      </div>
    </div>
  );
};
export default Card;
