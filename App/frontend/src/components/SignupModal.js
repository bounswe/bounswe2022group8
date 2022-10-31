import React, { useState, useReducer } from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
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
  const [responseStatus, setResponseStatus] = useState(0);

  const { saveToken } = useAuth();

  function handleSubmit(event) {
    event.preventDefault();

    fetch("http://44.211.68.74:8000/api/v1/auth/register/", {
      method: "POST",
      body: JSON.stringify(signupInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        setResponseStatus(response.status);
        props.onSubmitSignUp(response.status);
        return response.json();
      })
      .then((response) => {
        saveToken(response.token);
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
              responseStatus === 400 ? "form-control-error" : ""
            }`}
            placeholder="Username"
            id="username"
            required
            name="username"
            defaultValue={signupInput.username}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Email</label>
          <input
            type="email"
            className={`form-control mt-1 + ${
              responseStatus === 400 ? "form-control-error" : ""
            }`}
            placeholder="Email"
            id="email"
            required
            name="email"
            defaultValue={signupInput.email}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Password</label>
          <input
            type="password"
            className={`form-control mt-1 + ${
              responseStatus === 400 ? "form-control-error" : ""
            }`}
            placeholder="Choose a password"
            id="password"
            required
            name="password"
            defaultValue={signupInput.password}
            onChange={handleInput}
          />
        </div>
        <div className="form-group mt-3">
          <label className="access-label">Confirm password</label>
          <input
            type="password"
            className={`form-control mt-1 + ${
              responseStatus === 400 ? "form-control-error" : ""
            }`}
            placeholder="Confirm password"
            id="password_confirm"
            required
            name="password_confirm"
            defaultValue={signupInput.password_confirm}
            onChange={handleInput}
          />
        </div>
        {responseStatus === 400 && (
          <div>
            <div className="form-error">
              Please make sure to enter:<br></br> a unique username of at least
              6 characters,<br></br> a valid e-mail address,<br></br> and a
              password of at least 10 characters.
            </div>
          </div>
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
