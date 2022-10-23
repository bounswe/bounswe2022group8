import MainNavigation from "../layout/MainNavigation";
import Signup from "./Signup";
import Login from "./Login";
import Backdrop from "../components/Backdrop";
import { useState } from "react";

function Homepage() {
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

export default Homepage;
