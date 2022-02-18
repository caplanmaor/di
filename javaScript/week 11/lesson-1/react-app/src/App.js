import logo from './logo.svg';
import './App.css';
import Home from './components/Home';
import {Routes,Route} from 'react-router-dom'

function App() {
  return (
    <div className="App">
	  <Nav/>
	  <Home />
	  <About />
	  <LoginRegisterForm />
   </div>
  );
}

export default App;
