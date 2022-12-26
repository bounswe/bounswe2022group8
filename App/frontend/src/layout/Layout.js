import React, { useState, useEffect } from "react";
import Mainbar from "./Mainbar";
import MainbarLogged from "./MainbarLogged";
import Signup from "../components/SignupModal";
import Login from "../components/LoginModal";
import ResetPassword from "../components/ResetPasswordModal";
import Backdrop from "../components/Backdrop";
import Sidebar from "./Sidebar";
import { useAuth } from "../auth/authentication";

import { useNavigate } from "react-router-dom";

import "./styles/Layout.css";

function Layout(props) {
  function scrollToTop() {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "instant",
    });
  }

  const { token } = useAuth();

  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);
  const [resPassIsOpen, setResPassIsOpen] = useState(false);
  const [mainbarOpen, setMainbarOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  // const [currentScrollY, setCurrentScrollY] = useState(0);
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  const navigate = useNavigate();

  function handleSignUp() {
    setSignUpIsOpen(true);
    setLogInIsOpen(false);
  }

  // 2 UNNECESSARY RE-RENDERS --> BAD
  useEffect(() => {
    if (props.joinClicked) {
      handleSignUp();
      props.cancelJoinClick();
    }
  }, [props.joinClicked]);

  function handleLogIn() {
    setLogInIsOpen(true);
    setSignUpIsOpen(false);
  }

  // 2 UNNECESSARY RE-RENDERS --> BAD
  useEffect(() => {
    if (props.guestClick) {
      handleLogIn();
      props.cancelGuestClick();
    }
  }, [props.guestClick]);

  function handleResPass() {
    setResPassIsOpen(true);
    setLogInIsOpen(false);
  }

  function handleBackToLogIn() {
    setResPassIsOpen(false);
    setLogInIsOpen(true);
  }

  function handleCloseForm() {
    setSignUpIsOpen(false);
    setLogInIsOpen(false);
    setResPassIsOpen(false);
  }

  // when successfully signed up, close the sign up pop up and
  // close the sidebar if it was open
  function handleSubmitSignUp(response) {
    setSignUpIsOpen(response !== 201);
    if (response === 201) {
      setSidebarOpen(false);
      scrollToTop();
    }
  }

  // when successfully logged in, close the log in pop up and
  // close the sidebar if it was open
  function handleSubmitLogIn(response) {
    setLogInIsOpen(response !== 200);
    if (response === 200) {
      setSidebarOpen(false);
      scrollToTop();
    }
  }

  function handleClickLogOut() {
    window.location.replace("/");
    /*navigate("/");
    scrollToTop();*/
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

  function updateWidth() {
    setWindowWidth(window.innerWidth);
  }

  useEffect(() => {
    window.addEventListener("resize", updateWidth);
    return () => window.removeEventListener("resize", updateWidth);
  }, []);

  return (
    <div>
      {token ? (
        <MainbarLogged
          mainbarOpen={mainbarOpen}
          sidebarOpen={sidebarOpen}
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
          onClickResPass={() => handleResPass()}
          onClickClose={() => handleCloseForm()}
        />
      )}
      {resPassIsOpen && (
        <ResetPassword
          onClickClose={() => handleCloseForm()}
          onClickBack={() => handleBackToLogIn()}
        />
      )}
      {(signUpIsOpen || logInIsOpen || resPassIsOpen) && (
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
