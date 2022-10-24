import "./styles/Homepage.css";
import IntroImage from "../components/IntroImage";
import MainNavigation from "../layout/MainNavigation";
import Signup from "./Signup";
import Login from "./Login";
import Backdrop from "../components/Backdrop";
import { useState } from "react";

function Homepage(props) {
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
      <MainNavigation
        onSignUpClick={() => handleSignUp()}
        onLogInClick={() => handleLogIn()}
      />
      <IntroImage onJoinNowClick={() => handleSignUp()} />
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
      <div className="deneme">HOMEPAGE5</div>
    </div>
  );
}

export default Homepage;
