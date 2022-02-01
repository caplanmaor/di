import { connect } from "react-redux";
import { findMatch } from "../redux/actions";

const Calc = (props) => {
  return (
    <button onClick={() => props.handleClick(props.fname, props.sname)}>
      submit
    </button>
  );
};

const mapStateToProps = (state) => {
  return {
    fname: state.fname,
    sname: state.sname,
  };
};
const mapDispatchToProps = (dispatch) => {
  return {
    handleClick: (fname, sname) => dispatch(findMatch(fname, sname)),
  };
};
export default connect(null, mapDispatchToProps)(Calc);
