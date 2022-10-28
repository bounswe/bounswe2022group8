import React, { useState, useEffect } from "react";
import Mainbar from "./Mainbar";
import MainbarLogged from "./MainbarLogged";
import Signup from "../components/SignupModal";
import Login from "../components/LoginModal";
import Backdrop from "../components/Backdrop";
import Sidebar from "./Sidebar";

import "./styles/Layout.css";

function Layout(props) {
  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);
  const [mainbarOpen, setMainbarOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [currentScrollY, setCurrentScrollY] = useState(0);

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
    handleLogIn();
  }

  function handleSubmitLogIn() {
    setLogInIsOpen(false);
  }

  function handleSidebar() {
    setSidebarOpen(!sidebarOpen);
  }

  useEffect(() => {
    function changeNavbarColor() {
      if (window.scrollY >= 30) {
        setMainbarOpen(true);
      } else {
        setMainbarOpen(false);
      }
    }
    window.addEventListener("scroll", changeNavbarColor);

    return () => window.removeEventListener("scroll", changeNavbarColor);
  }, []);

  // keeps track of the current position of the scrollbar
  useEffect(() => {
    function updatePosition() {
      setCurrentScrollY(window.scrollY);
    }
    window.addEventListener("scroll", updatePosition);
    return () => window.removeEventListener("scroll", updatePosition);
  }, []);

  // prevents scrollbar to reset each time a component re-renders
  useEffect(() => {
    window.scrollTo(0, currentScrollY);
  }, [currentScrollY]);

  return (
    <div>
      <Mainbar
        mainbarOpen={mainbarOpen}
        sidebarOpen={sidebarOpen}
        onClickLogIn={() => handleLogIn()}
        onClickSignUp={() => handleSignUp()}
        onClickMenu={() => handleSidebar()}
      />
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
      <main
        className="main-container"
        style={{
          marginRight: sidebarOpen ? "300px" : "0px",
          //opacity: sidebarOpen ? "0.6" : "1",
        }}
      >
        {props.children}
      </main>
    </div>
  );
}

export default Layout;
