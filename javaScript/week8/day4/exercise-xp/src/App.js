import logo from "./logo.svg";
import "./App.css";
import { Route, Routes, Link } from "react-router-dom";
import ErrorBoundary from "./components/ErrorBoundary";
import "bootstrap/dist/css/bootstrap.css";
import {
  Container,
  Navbar,
  NavItem,
  NavDropdown,
  MenuItem,
  Nav,
} from "react-bootstrap";
import PostList from "./components/PostList";

const Home = () => (
  <div>
    <h1>HomePage</h1>
    <img
      src="https://cdn.pixabay.com/photo/2018/05/18/15/30/webdesign-3411373_1280.jpg"
      alt="Homepage"
      width="40%"
    />
  </div>
);

const Profile = () => (
  <div>
    <h1>Profile me : My Hobbies</h1>
    <img
      src="https://cdn.pixabay.com/photo/2017/06/16/18/03/classical-2409809_1280.png"
      alt="Profile"
      width="40%"
    />
    <p>I love playing the guitar!</p>
  </div>
);

const Shop = () => (
  <div>
    <h1>Here is a list of projects</h1>
    <img
      src=" https://cdn.pixabay.com/photo/2017/06/10/07/18/list-2389219_1280.png"
      alt="Shop"
      width="30%"
    />
  </div>
);

const App = () => {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="/">React-Bootstrap</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <ErrorBoundary>
                <Nav.Link href="/">Home</Nav.Link>
              </ErrorBoundary>
              <ErrorBoundary>
                <Nav.Link href="/profile">Profile</Nav.Link>
              </ErrorBoundary>
              <ErrorBoundary>
                <Nav.Link href="/shop">Shop</Nav.Link>
              </ErrorBoundary>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <PostList />

      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/shop" element={<Shop />} />
      </Routes>
    </div>
  );
};

export default App;
