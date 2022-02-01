import { connect } from "react-redux";
import { setNames } from "../redux/actions";

const Fname = (props) => {
  return (
    <div>
      First Name:
      <input type="text" name="fname" onChange={props.handleChange} />
    </div>
  );
};

const mapDispatchToProps = (dispatch) => {
  return {
    handleChange: (e) => dispatch(setNames(e.target.name, e.target.value)),
  };
};
export default connect(null, mapDispatchToProps)(Fname);
