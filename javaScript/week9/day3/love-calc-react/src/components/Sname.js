import { connect } from "react-redux";
import { setNames } from "../redux/actions";

const Sname = (props) => {
  return (
    <div>
      Second Name:
      <input type="text" name="sname" onChange={props.handleChange} />
    </div>
  );
};
const mapDispatchToProps = (dispatch) => {
  return {
    handleChange: (e) => dispatch(setNames(e.target.name, e.target.value)),
  };
};
export default connect(null, mapDispatchToProps)(Sname);
