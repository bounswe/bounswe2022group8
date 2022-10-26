import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Searchbar from "../components/Searchbar";
import MenuButton from "../components/MenuButton";
import React, { useState, useEffect } from "react";
import Signup from "../components/SignupModal";
import Login from "../components/LoginModal";
import Backdrop from "../components/Backdrop";
import Sidebar from "./Sidebar";
import "./styles/MainNavigation.css";

function MainNavigation(props) {
  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);
  const [navbarColor, setNavbarColor] = useState(0);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  function handleSignUp() {
    setSignUpIsOpen(true);
    setLogInIsOpen(false);
  }

  function handleLogIn() {
    setLogInIsOpen(true);
    setSignUpIsOpen(false);
  }

  function handleCloseForm() {
    setSignUpIsOpen(false);
    setLogInIsOpen(false);
  }

  function handleSubmitSignUp() {
    setSignUpIsOpen(false);
  }

  function handleSubmitLogIn() {
    setLogInIsOpen(false);
  }

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

  function handleSidebar() {
    setSidebarOpen(!sidebarOpen);
  }

  return (
    <div>
      <Navbar
        sticky="top"
        expand="md"
        className={
          navbarColor ? "navigation-bar navigation-bar-bg" : "navigation-bar"
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
                  !navbarColor && sidebarOpen
                    ? "me-3 btn-access-sidebar"
                    : "me-3 btn-access"
                }
                onClick={() => handleLogIn()}
              >
                Log in
              </Button>
            </Nav>
            <Nav>
              <Button
                as="a"
                variant=""
                className={
                  !navbarColor && sidebarOpen
                    ? "me-3 btn-access-sidebar"
                    : "me-3 btn-access"
                }
                onClick={() => handleSignUp()}
              >
                Sign up
              </Button>
            </Nav>
            <Nav>
              <MenuButton
                onClick={() => handleSidebar()}
                rotate={sidebarOpen ? "rotate(90deg)" : "rotate(0)"}
                sidebarStyle={!navbarColor && sidebarOpen ? true : false}
              />
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      {signUpIsOpen && (
        <Signup
          onSubmitSignUp={() => handleSubmitSignUp()}
          onClickLogIn={() => handleLogIn()}
          onClickClose={() => handleCloseForm()}
        />
      )}
      {logInIsOpen && (
        <Login
          onSubmitLogIn={() => handleSubmitLogIn()}
          onClickSignUp={() => handleSignUp()}
          onClickClose={() => handleCloseForm()}
        />
      )}
      {(signUpIsOpen || logInIsOpen) && (
        <Backdrop onClick={() => handleCloseForm()} />
      )}
      <Sidebar width={sidebarOpen ? "300px" : "0px"} />
    </div>
  );
}

export default MainNavigation;
