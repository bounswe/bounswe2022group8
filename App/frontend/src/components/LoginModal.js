import React, { useState, useReducer } from "react";
import { Link } from "react-router-dom";
import CloseButton from "react-bootstrap/CloseButton";
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
  const [responseStatus, setResponseStatus] = useState(0);

  const { saveToken } = useAuth();

  function handleSubmit(event) {
    event.preventDefault();

    fetch("http://34.125.134.88:8000/api/v1/auth/login/", {
      method: "POST",
      body: JSON.stringify(loginInput),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        setResponseStatus(response.status);
        props.onSubmitLogIn(response.status);
        return response.json();
      })
      .then((response) => {
        saveToken(response.token);
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
              responseStatus === 400 ? "form-control-error" : ""
            }`}
            placeholder="Email or username"
            name="credential"
            id="credential"
            required
            defaultValue={loginInput.credential}
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
            placeholder="Password"
            name="password"
            id="password"
            required
            defaultValue={loginInput.password}
            onChange={handleInput}
          />
        </div>
        {responseStatus === 400 && (
          <div className="form-error">
            Please check your input and try again.
          </div>
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
          <Link to="./">Forgot password?</Link>
        </p>
        <p className="text-center mt-2">
          Not on (AppName) yet?{" "}
          <Link onClick={props.onClickSignUp}>Sign up</Link>
        </p>
      </div>
    </form>
  );
}

export default Login;
