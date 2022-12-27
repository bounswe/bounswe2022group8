import React, { useState, useReducer } from "react";
import { Link, useNavigate } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import { HOST } from "../constants/host";
import "./styles/Access.css";

import { useAuth } from "../auth/authentication";

function Login(props) {
  const [loginInput, setLoginInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    {
      credential: "",
      password: "",
    }
  );

  const [credentialEmpty, setCredentialEmpty] = useState(false);
  const [passwordEmpty, setPasswordEmpty] = useState(false);
  const [credentialIncorrect, setCredentialIncorrect] = useState(false);
  const [passwordIncorrect, setPasswordIncorrect] = useState(false);

  var host = HOST;
  const { saveToken } = useAuth();
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();

    fetch(`${host}/api/v1/auth/login/`, {
      method: "POST",
      body: JSON.stringify(loginInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        props.onSubmitLogIn(response.status);
        return response.json();
      })
      .then((response) => {
        response.credential
          ? setCredentialEmpty(true)
          : setCredentialEmpty(false);

        response.password ? setPasswordEmpty(true) : setPasswordEmpty(false);

        response.credentials &&
        response.credentials[0] === "Incorrect username or email."
          ? setCredentialIncorrect(true)
          : setCredentialIncorrect(false);

        response.credentials &&
        response.credentials[0] === "Incorrect password."
          ? setPasswordIncorrect(true)
          : setPasswordIncorrect(false);

        if (response.token) {
          saveToken(response.token);
          navigate("/discover");
        }
      })
      .catch((error) => console.error("Error:", error));
  }

  const handleInput = (event) => {
    const name = event.target.name;
    const newValue = event.target.value;
    setLoginInput({ [name]: newValue });
  };

  // console.log(responseStatus);

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Log In</h3>
        <div className="form-group mt-3">
          <label className="access-label">Email or username</label>
          <input
            type="email"
            className={`form-control mt-1 + ${
              credentialEmpty || credentialIncorrect ? "form-control-error" : ""
            }`}
            placeholder="Email or username"
            name="credential"
            id="credential"
            required
            defaultValue={loginInput.credential}
            onChange={handleInput}
          />
        </div>
        {credentialEmpty && (
          <div className="form-error">Please fill in this field.</div>
        )}
        {credentialIncorrect && (
          <div className="form-error">Incorrect email or username.</div>
        )}
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className={`form-control mt-1 + ${
              passwordEmpty || passwordIncorrect ? "form-control-error" : ""
            }`}
            placeholder="Password"
            name="password"
            id="password"
            required
            defaultValue={loginInput.password}
            onChange={handleInput}
          />
        </div>
        {passwordEmpty && (
          <div className="form-error">Please fill in this field.</div>
        )}
        {passwordIncorrect && (
          <div className="form-error">Incorrect password.</div>
        )}
        <div className="d-grid gap-2 mt-4">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Log in
          </button>
        </div>
        <p className="forgot-password text-center mt-3">
          <Link onClick={props.onClickResPass} className="access-link">
            Forgot password?
          </Link>
        </p>
        <p className="text-center mt-2">
          Not on Artopia yet?{" "}
          <Link onClick={props.onClickSignUp} className="access-link">
            Sign up
          </Link>
        </p>
      </div>
    </form>
  );
}

export default Login;
