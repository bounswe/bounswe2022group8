import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import SearchBar from "../components/SearchBar";
import MenuButton from "../components/MenuButton";

function MainNavigation(props) {
  return (
    <Navbar expand="md" style={{ height: 70 }} bg="light" variant="light">
      <Container fluid>
        <Navbar.Brand className="ms-4 me-5" href="./">
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
          <Button
            as="a"
            variant="outline-primary"
            className="me-3"
            onClick={props.onLogInClick}
          >
            Log in
          </Button>
        </Nav>
        <Nav>
          <MenuButton/>
        </Nav>
      </Container>
    </Navbar>
  );
}

export default MainNavigation;
