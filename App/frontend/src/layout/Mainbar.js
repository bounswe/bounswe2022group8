import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Searchbar from "../components/Searchbar";
import MenuButton from "../components/MenuButton";
import React from "react";
import "./styles/Mainbar.css";

function Mainbar(props) {
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
        <Navbar.Brand
          className="ms-4 me-5"
          href="./"
          style={{ color: "white" }}
        >
          App Name
        </Navbar.Brand>
        <Navbar.Collapse>
          <Nav className="me-auto">
            <Searchbar />
          </Nav>

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
              rotate={props.BackdropsidebarOpen ? "rotate(90deg)" : "rotate(0)"}
              sidebarStyle={
                !props.mainbarOpen && props.sidebarOpen ? true : false
              }
            />
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Mainbar;
