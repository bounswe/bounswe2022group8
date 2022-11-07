import React, { useState, useEffect } from "react";
import Mainbar from "./Mainbar";
import MainbarLogged from "./MainbarLogged";
import Signup from "../components/SignupModal";
import Login from "../components/LoginModal";
import Backdrop from "../components/Backdrop";
import Sidebar from "./Sidebar";
import { useAuth } from "../auth/authentication";

import { useNavigate } from "react-router-dom";

import "./styles/Layout.css";

function Layout(props) {
  const { token } = useAuth();

  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);
  const [mainbarOpen, setMainbarOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  // const [currentScrollY, setCurrentScrollY] = useState(0);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  const navigate = useNavigate();

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

  function handleSubmitSignUp(response) {
    setSignUpIsOpen(response !== 201);
  }

  function handleSubmitLogIn(response) {
    setLogInIsOpen(response !== 200);
  }

  function handleSidebar() {
    setSidebarOpen(!sidebarOpen);
  }

  function goToProfile(){
    navigate('/:username');
  }

  // changes color of the navbar w.r.t scrollY position
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

  /*// keeps track of the current position of the scrollbar
  function updatePosition() {
    setCurrentScrollY(window.scrollY);
  }

  useEffect(() => {
    window.addEventListener("scroll", updatePosition);
    return () => window.removeEventListener("scroll", updatePosition);
  }, []);

  // prevents scrollbar to reset each time a component re-renders
  useEffect(() => {
    window.scrollTo(0, currentScrollY);
  }, [currentScrollY]);*/

  // keeps track of the current windows width

  function updateWidth() {
    setWindowWidth(window.innerWidth);
  }

  useEffect(() => {
    window.addEventListener("resize", updateWidth);
    return () => window.removeEventListener("resize", updateWidth);
  }, []);

  // console.log(windowWidth);

  return (
    <div>
      {token ? (
        <MainbarLogged
          mainbarOpen={mainbarOpen}
          sidebarOpen={sidebarOpen}
          onClickLogIn={() => handleLogIn()}
          onClickSignUp={() => handleSignUp()}
          onClickMenu={() => handleSidebar()}
          onClickProfile={() => goToProfile()}
        />
      ) : (
        <Mainbar
          mainbarOpen={mainbarOpen}
          sidebarOpen={sidebarOpen}
          onClickLogIn={() => handleLogIn()}
          onClickSignUp={() => handleSignUp()}
          onClickMenu={() => handleSidebar()}
        />
      )}

      {signUpIsOpen && (
        <Signup
          onSubmitSignUp={(response) => handleSubmitSignUp(response)}
          onClickLogIn={() => handleLogIn()}
          onClickClose={() => handleCloseForm()}
        />
      )}
      {logInIsOpen && (
        <Login
          onSubmitLogIn={(response) => handleSubmitLogIn(response)}
          onClickSignUp={() => handleSignUp()}
          onClickClose={() => handleCloseForm()}
        />
      )}
      {(signUpIsOpen || logInIsOpen) && (
        <Backdrop onClick={() => handleCloseForm()} />
      )}
      <Sidebar width={sidebarOpen ? "300px" : "0px"} auth={token} />
      <main
        className="main-container"
        style={{
          marginRight: sidebarOpen && windowWidth >= 1400 ? "300px" : "0px",
        }}
      >
        {props.children}
      </main>
    </div>
  );
}

export default Layout;
