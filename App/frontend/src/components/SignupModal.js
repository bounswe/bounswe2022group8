import React, { useState, useReducer } from "react";
import { Link, useNavigate } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
import { HOST } from "../constants/host";
import "./styles/Access.css";

import { useAuth } from "../auth/authentication";

function Signup(props) {
  const [signupInput, setSignupInput] = useReducer(
    (state, newState) => ({ ...state, ...newState }),
    {
      email: "",
      username: "",
      password: "",
      password_confirm: "",
    }
  );

  const [usernameError, setUsernameError] = useState(null);
  const [emailError, setEmailError] = useState(null);
  const [passwordError, setPasswordError] = useState(null);
  const [confirmPasswordError, setConfirmPasswordError] = useState(null);

  const { saveToken } = useAuth();
  const navigate = useNavigate();

  function handleSubmit(event) {
    event.preventDefault();
    var host = HOST;

    fetch(`${host}/api/v1/auth/register/`, {
      method: "POST",
      body: JSON.stringify(signupInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        props.onSubmitSignUp(response.status);
        return response.json();
      })
      .then((response) => {
        response.username
          ? setUsernameError(response.username[0])
          : setUsernameError(null);

        response.email ? setEmailError(response.email[0]) : setEmailError(null);

        response.password
          ? setPasswordError(response.password[0])
          : setPasswordError(null);

        response.password_confirm
          ? setConfirmPasswordError(response.password_confirm[0])
          : setConfirmPasswordError(null);

        if (response.token) {
          saveToken(response.token);
          navigate("/discover");
        }
      })
      .catch((error) => console.error("Error:", error));
  }

  const handleInput = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setSignupInput({ [name]: value });
  };

  return (
    <form className="access">
      <div className="access-btn-close">
        <CloseButton onClick={props.onClickClose} />
      </div>
      <div className="access-content">
        <h3 className="access-title">Sign Up</h3>
        <div className="text-center">
          Already registered? <Link onClick={props.onClickLogIn}>Log in</Link>
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Username</label>
          <input
            type="text"
            className={`form-control mt-1 + ${
              usernameError ? "form-control-error" : ""
            }`}
            placeholder="Username"
            id="username"
            required
            name="username"
            defaultValue={signupInput.username}
            onChange={handleInput}
          />
        </div>
        {usernameError && <div className="form-error">{usernameError}</div>}
        <div className="form-group mt-3">
          <label className="access-label">Email</label>
          <input
            type="email"
            className={`form-control mt-1 + ${
              emailError ? "form-control-error" : ""
            }`}
            placeholder="Email"
            id="email"
            required
            name="email"
            defaultValue={signupInput.email}
            onChange={handleInput}
          />
        </div>
        {emailError && <div className="form-error">{emailError}</div>}
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className={`form-control mt-1 + ${
              passwordError ? "form-control-error" : ""
            }`}
            placeholder="Choose a password"
            id="password"
            required
            name="password"
            defaultValue={signupInput.password}
            onChange={handleInput}
          />
        </div>
        {passwordError && <div className="form-error">{passwordError}</div>}
        <div className="form-group mt-3">
          <label className="access-label">Confirm password</label>
          <input
            type="password"
            className={`form-control mt-1 + ${
              confirmPasswordError ? "form-control-error" : ""
            }`}
            placeholder="Confirm password"
            id="password_confirm"
            required
            name="password_confirm"
            defaultValue={signupInput.password_confirm}
            onChange={handleInput}
          />
        </div>
        {confirmPasswordError && (
          <div className="form-error">{confirmPasswordError}</div>
        )}
        <div className="d-grid gap-2 mt-4 mb-4">
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Sign Up
          </button>
        </div>
      </div>
    </form>
  );
}

export default Signup;
