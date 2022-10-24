import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import SearchBar from "../components/SearchBar";
import MenuButton from "../components/MenuButton";
import React, { useState, useEffect } from "react";
import "./styles/MainNavigation.css";

function MainNavigation(props) {
  const [navbarColor, setNavbarColor] = useState(0);

  const changeNavbarColor = () => {
    if (window.scrollY >= 30) {
      setNavbarColor(true);
    } else {
      setNavbarColor(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", changeNavbarColor);

    return () => {
      window.removeEventListener("scroll", changeNavbarColor);
    };
  }, []);

  return (
    <Navbar
      sticky="top"
      expand="md"
      className={navbarColor ? "navbar navbar-bg" : "navbar"}
    >
      <Container fluid>
        <Navbar.Brand
          className="ms-4 me-5"
          href="./"
          style={{ color: "white" }}
        >
          App Name
        </Navbar.Brand>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <SearchBar />
          </Nav>

          <Nav className="ms-auto">
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
            <MenuButton />
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default MainNavigation;
