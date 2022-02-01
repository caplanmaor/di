import "./App.css";
import { useSelector, useDispatch } from "react-redux";
import { decrement, increment, reset, logIn, logOut } from "./actions/index.js";

function App() {
  const counter = useSelector((state) => state.counter);
  const auth = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>redux counter</h1>
      <h3>Counter</h3>
      <h3>{counter}</h3>
      <button onClick={() => dispatch(increment())}>increase</button>
      <button onClick={() => dispatch(reset())}>reset</button>
      <button onClick={() => dispatch(decrement())}>decrement</button>

      <h2>for logged in users only</h2>
      <p>log in to see secret information</p>
      <button onClick={() => dispatch(logIn())}>log in</button>
      <button onClick={() => dispatch(logOut())}>log out</button>
      {auth ? (
        <div>
          <p>redux is awesome</p>
        </div>
      ) : (
        ""
      )}
    </div>
  );
}

export default App;
