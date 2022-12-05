import React from "react";
import { Link } from "react-router-dom";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Searchbar from "../components/Searchbar";
import MenuButton from "../components/MenuButton";

import "./styles/Mainbar.css";
import artopia_logo from "../images/artopia_logo.png";

function Mainbar(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  return (
    <Navbar
      sticky="top"
      expand="md"
      className={
        props.mainbarOpen
          ? "navigation-bar navigation-bar-bg"
          : "navigation-bar"
      }
    >
      <Container fluid>
        <Link to="/" onClick={scrollToTop} style={{ textDecoration: "none" }}>
          <Navbar.Brand className="ms-4 me-5" style={{ color: "white" }}>
            <img className="logo-image" src={artopia_logo} alt="logo" />
          </Navbar.Brand>
        </Link>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <Searchbar />
          </Nav>
        </Navbar.Collapse>
        <Nav className="ms-auto">
          <Button
            as="a"
            variant=""
            className={
              !props.mainbarOpen && props.sidebarOpen
                ? "me-3 btn-access-sidebar"
                : "me-3 btn-access"
            }
            onClick={props.onClickLogIn}
          >
            Log in
          </Button>
        </Nav>
        <Nav>
          <Button
            as="a"
            variant=""
            className={
              !props.mainbarOpen && props.sidebarOpen
                ? "me-3 btn-access-sidebar"
                : "me-3 btn-access"
            }
            onClick={props.onClickSignUp}
          >
            Sign up
          </Button>
        </Nav>
        <Nav>
          <MenuButton
            onClick={props.onClickMenu}
            rotate={props.sidebarOpen ? "rotate(90deg)" : "rotate(0)"}
            sidebarStyle={
              !props.mainbarOpen && props.sidebarOpen ? true : false
            }
          />
        </Nav>
      </Container>
    </Navbar>
  );
}

export default Mainbar;
