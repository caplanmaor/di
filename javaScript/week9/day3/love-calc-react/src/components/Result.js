import { connect } from "react-redux";

const Result = (props) => {
  return (
    <div>
      Results:
      <p>
        {props.results.fname} & {props.results.sname}
      </p>
      <p>percentage: {props.results.percentage}</p>
      <p>result: {props.results.result}</p>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    results: state.results,
  };
};

export default connect(mapStateToProps)(Result);
