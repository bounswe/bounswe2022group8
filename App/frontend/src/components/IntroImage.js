import "./styles/IntroImage.css";
import background from "../media/aurora.jpg";
import Button from "react-bootstrap/Button";
import React, { useState } from "react";
import Signup from "./SignupModal";
import Login from "./LoginModal";
import Backdrop from "../components/Backdrop";

function IntroImage(props) {
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
      <div className="background-image-container">
        <img className="background-image" src={background} alt="Aurora" />
        <div className="input-on-background-image">
          <div className="text-on-background-image">
            <p className="main-header"> PRESENT, MANAGE AND SELL YOUR ART </p>
            <p>
              Revolutionize the way you promote your art online – with APPNAME
              tools.
            </p>
          </div>
          <div className="btn-on-background-image-container">
            <Button
              className="btn-on-background-image"
              as="a"
              variant=""
              onClick={() => handleSignUp()}
            >
              JOIN NOW
            </Button>
          </div>
        </div>
      </div>
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
    </div>
  );
}

export default IntroImage;
