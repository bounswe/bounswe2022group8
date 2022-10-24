import MainNavigation from "./MainNavigation";
import Signup from "../pages/Signup";
import Login from "../pages/Login";
import Backdrop from "../components/Backdrop";
import "./styles/Layout.css";
import { useState } from "react";

function Layout(props) {
  const [signUpIsOpen, setSignUpIsOpen] = useState(false);
  const [logInIsOpen, setLogInIsOpen] = useState(false);

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

  return (
    <div>
      <MainNavigation
        onSignUpClick={() => handleSignUp()}
        onLogInClick={() => handleLogIn()}
      />
      <main className="layout-main">{props.children}</main>
      {signUpIsOpen && (
        <Signup
          onSubmitSignUp={() => handleSubmitSignUp()}
          onClickLogIn={() => handleLogIn()}
        />
      )}
      {logInIsOpen && (
        <Login
          onSubmitLogIn={() => handleSubmitLogIn()}
          onClickSignUp={() => handleSignUp()}
        />
      )}
      {(signUpIsOpen || logInIsOpen) && (
        <Backdrop onClick={() => handleCloseForm()} />
      )}
    </div>
  );
}

export default Layout;
