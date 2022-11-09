import React, { useState, useEffect } from "react";
import Mainbar from "./Mainbar";
import MainbarLogged from "./MainbarLogged";
import Signup from "../components/SignupModal";
import Login from "../components/LoginModal";
import Backdrop from "../components/Backdrop";
import Sidebar from "./Sidebar";
import { useAuth } from "../auth/authentication";

import "./styles/Layout.css";

function Layout(props) {
  const { token } = useAuth();

  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);
  const [mainbarOpen, setMainbarOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  // const [currentScrollY, setCurrentScrollY] = useState(0);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

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

  // when successfully signed up, close the sign up pop up and
  // close the sidebar if it was open
  function handleSubmitSignUp(response) {
    setSignUpIsOpen(response !== 201);
    if (response === 201) setSidebarOpen(false);
  }

  // when successfully logged in, close the log in pop up and
  // close the sidebar if it was open
  function handleSubmitLogIn(response) {
    setLogInIsOpen(response !== 200);
    if (response === 200) setSidebarOpen(false);
  }

  // when log out is clicked, re-render server side and redirect to home page
  function handleClickLogOut() {
    window.location.replace("./");  // window.location.href("./") might also be used
  }

  function handleSidebar() {
    setSidebarOpen(!sidebarOpen);
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
      <Sidebar
        onClickLogOut={() => handleClickLogOut()}
        width={sidebarOpen ? "300px" : "0px"}
        auth={token}
      />
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
