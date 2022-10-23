import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import SearchBar from "../components/SearchBar";

function MainNavigation(props) {
  return (
    <Navbar expand="md" style={{ height: 70 }} bg="light" variant="light">
      <Container>
        <Navbar.Brand className="me-5" href="./">
          App Name
        </Navbar.Brand>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <SearchBar />
          </Nav>
        </Navbar.Collapse>
        <Nav className="ms-auto">
          <Button
            as="a"
            variant="outline-primary"
            className="me-3"
            onClick={props.onSignUpClick}
          >
            Sign up
          </Button>
        </Nav>
        <Nav>
          <Button as="a" variant="outline-primary" onClick={props.onLogInClick}>
            Log in
          </Button>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default MainNavigation;
